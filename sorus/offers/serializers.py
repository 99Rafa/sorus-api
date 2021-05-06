from rest_framework import serializers

from offers.models import Product, Review


class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['date', 'rate', 'title', 'comment', 'product', 'user']


class CreateOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'start_date', 'end_date', 'promoter_id', 'state']
