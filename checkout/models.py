from django.db import models
from django.contrib.auth import get_user_model

# Get the user model
User = get_user_model()


# Billing Address Model
class BillingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    landmark = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.user.username} billing address'

    class Meta:
        verbose_name_plural = "Billing Addresses"
