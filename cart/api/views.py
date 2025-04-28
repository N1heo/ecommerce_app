from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from cart.models import CartItem, Order
from product.models import Product
from .serializers import CartItemSerializer, OrderSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cart_view(request):
    user = request.user
    orders = Order.objects.filter(user=user, ordered=False)

    if not orders.exists():
        return Response({"detail": "You do not have an active order."}, status=404)

    order = orders.first()
    carts = CartItem.objects.filter(user=user, order=order)
    cart_data = CartItemSerializer(carts, many=True).data
    order_data = OrderSerializer(order).data

    return Response({
        "cart": order_data
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    user = request.user
    order, created = Order.objects.get_or_create(user=user, ordered=False)
    cart_item_qs = CartItem.objects.filter(user=user, item=item, order=order, purchased=False)

    if cart_item_qs.exists():
        cart_item = cart_item_qs.first()
        cart_item.quantity += 1
        cart_item.save()
        message = "This item quantity was updated."
    else:
        CartItem.objects.create(user=user, item=item, quantity=1, order=order)
        message = "This item was added to your cart."

    return Response({"message": message})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def decrease_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    user = request.user

    order_qs = Order.objects.filter(user=user, ordered=False)
    if not order_qs.exists():
        return Response({"detail": "You do not have an active order."}, status=400)

    order = order_qs.first()
    cart_item_qs = CartItem.objects.filter(user=user, item=item, order=order)

    if not cart_item_qs.exists():
        return Response({"detail": f"{item.name} is not in your cart."}, status=400)

    cart_item = cart_item_qs.first()
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        return Response({"message": f"{item.name} quantity has been updated."})
    else:
        cart_item.delete()
        return Response({"message": f"{item.name} was removed from your cart."})


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    user = request.user

    order_qs = Order.objects.filter(user=user, ordered=False)
    if not order_qs.exists():
        return Response({"detail": "You do not have an active order."}, status=400)

    order = order_qs.first()
    cart_item_qs = CartItem.objects.filter(user=user, item=item, order=order)

    if not cart_item_qs.exists():
        return Response({"detail": "This item was not in your cart."}, status=400)

    cart_item_qs.delete()
    return Response({"message": f"{item.name} was removed from your cart."})
