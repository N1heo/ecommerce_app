from django.urls import path
from checkout.api.views import (
    billing_address_view,
    create_stripe_session,
    stripe_success_view,
    stripe_cancel_view,
    order_history_view,
)
from checkout.api.views import stripe_webhook_view

app_name = "checkout"

urlpatterns = [
    path('webhook/stripe/', stripe_webhook_view, name='stripe-webhook'),

    path('checkout/address/', billing_address_view, name='api-billing-address'),
    path('checkout/payment/', create_stripe_session, name='api-checkout-payment'),
    path('checkout/success/', stripe_success_view, name='api-checkout-success'),
    path('checkout/cancel/', stripe_cancel_view, name='api-checkout-cancel'),
    path('checkout/orders/', order_history_view, name='api-checkout-orders'),
]
