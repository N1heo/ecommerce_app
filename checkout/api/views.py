from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.utils.crypto import get_random_string
from django.conf import settings
from django.urls import reverse


import stripe

from cart.api.serializers import OrderSerializer
from cart.models import Order, CartItem
from checkout.models import BillingAddress
from checkout.api.serializers import BillingAddressSerializer

stripe.api_key = settings.STRIPE_SECRET_KEY


@swagger_auto_schema(method='post', request_body=BillingAddressSerializer)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def billing_address_view(request):
    user = request.user
    try:
        address = BillingAddress.objects.get(user=user)
    except BillingAddress.DoesNotExist:
        address = None

    if request.method == 'GET':
        if address:
            serializer = BillingAddressSerializer(address)
            return Response(serializer.data)
        return Response({"detail": "No billing address found."}, status=404)

    elif request.method == 'POST':
        serializer = BillingAddressSerializer(instance=address, data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_stripe_session(request):
    user = request.user
    order_qs = Order.objects.filter(user=user, ordered=False)
    if not order_qs.exists():
        return Response({"error": "No active order found."}, status=404)

    order = order_qs.first()
    total_cents = int(order.get_total() * 100)

    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': f'Order by {user.username}',
                    },
                    'unit_amount': total_cents,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('checkout:api-checkout-success')),
            cancel_url=request.build_absolute_uri(reverse('checkout:api-checkout-cancel')),
            metadata={
                "user_id": str(user.id),
                "order_id": str(order.id),
            }
        )
        return Response({"checkout_url": checkout_session.url})
    except stripe.error.StripeError as e:
        return Response({"error": str(e)}, status=500)


@csrf_exempt
@api_view(['POST'])  # no auth needed, Stripe is the sender
@permission_classes([AllowAny])
def stripe_webhook_view(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError as e:
        return Response({'error': 'Invalid payload'}, status=400)
    except stripe.error.SignatureVerificationError as e:
        return Response({'error': 'Invalid signature'}, status=400)

    # Handle successful payment
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        user_id = session['metadata']['user_id']
        order_id = session['metadata']['order_id']

        try:
            order = Order.objects.get(id=order_id, user_id=user_id)
            if not order.ordered:
                order.ordered = True
                order.payment_id = session.get('payment_intent')
                order.order_id = f'#{order.user.username}{order.id}'
                order.save()

                CartItem.objects.filter(order=order).update(purchased=True)

        except Order.DoesNotExist:
            return Response({'error': 'Order not found'}, status=404)

    return Response({'status': 'success'})


@api_view(['GET'])
@permission_classes([])  # No auth required
def stripe_success_view(request):
    return Response({"message": "Thank you for your payment! Your order will be processed shortly."})


@api_view(['GET'])
@permission_classes([])
def stripe_cancel_view(request):
    return Response({"message": "Payment canceled by user."})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_history_view(request):
    orders = Order.objects.filter(user=request.user, ordered=True)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
