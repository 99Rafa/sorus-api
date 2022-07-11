from rest_framework import serializers

from sales.models import Sale
from users.models import User
from offers.models import Product


class CreateSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['quantity', 'price', 'buy_method', 'buy_date', 'buyer', 'product', 'reference']


class UpdateUserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['subscription']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'image', 'price']


class ListUserBuysSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)

    class Meta:
        model = Sale
        fields = ['reference', 'product', 'buy_date']