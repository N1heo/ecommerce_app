from rest_framework import serializers

from cart.models import CartItem, Order
from product.models import Product


class ProductMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'slug']


class CartItemSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()
    item = ProductMiniSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'user', 'item', 'quantity', 'created_at', 'order', 'purchased', 'total']

    def get_total(self, obj):
        return obj.get_total()


class OrderSerializer(serializers.ModelSerializer):
    order_items = CartItemSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'user', 'ordered', 'created_at', 'payment_id', 'order_id', 'order_items', 'total']

    def get_total(self, obj):
        return obj.get_total()
