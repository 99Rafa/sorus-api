from rest_framework import serializers

from sales.models import Sale


class CreateSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['quantity', 'price', 'buy_method', 'buy_date', 'buyer', 'product']