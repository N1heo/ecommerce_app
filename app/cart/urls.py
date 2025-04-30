from django.urls import path
from cart.api import views as api_views

app_name = 'cart-app'

urlpatterns = [
    path('cart/', api_views.cart_view, name='api-cart-view'),
    path('cart/add/<slug:slug>/', api_views.add_to_cart, name='api-add-to-cart'),
    path('cart/decrease/<slug:slug>/', api_views.decrease_cart, name='api-decrease-cart'),
    path('cart/remove/<slug:slug>/', api_views.remove_from_cart, name='api-remove-cart'),
]
