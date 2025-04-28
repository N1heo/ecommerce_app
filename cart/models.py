from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import localtime

from product.models import Product

# Get the user model
User = get_user_model()


# Order Model
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_id = models.TextField(blank=True, null=True)
    order_id = models.TextField(blank=True, null=True)

    def get_total(self):
        total = 0
        for order_item in self.order_items.all():
            total += order_item.get_total()

        return total

    def __str__(self):
        status = "✓" if self.ordered else "✗"
        date = localtime(self.created_at).strftime('%Y-%m-%d %H:%M')
        return f'[{status}] {self.user.username} - {self.order_id or "no-id"} - {date}'


# Cart Model
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, related_name='order_items')
    purchased = models.BooleanField(default=False)

    def get_total(self):
        total = self.item.price * self.quantity
        float_total = float("{0:.2f}".format(total))
        return float_total

    def __str__(self):
        return f'{self.quantity} of {self.item.name}'
