from rest_framework import serializers

from checkout.models import BillingAddress


class BillingAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = BillingAddress
        fields = ['address', 'zipcode', 'city', 'landmark']
