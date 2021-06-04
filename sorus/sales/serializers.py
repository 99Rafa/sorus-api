from rest_framework import serializers

from sales.models import Sale
from users.models import User


class CreateSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['quantity', 'price', 'buy_method', 'buy_date', 'buyer', 'product']


class UpdateUserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['subscription']