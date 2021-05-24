from rest_framework import serializers

from offers.models import Product, Review, Category


class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['date', 'rate', 'title', 'comment', 'product', 'user']


class CreateOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'start_date', 'end_date', 'promoter', 'state']


class ListOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image',
                  'start_date', 'end_date', 'time_left', 'still_active', 'category']


class UpdateOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'end_date', 'category']


class ListCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'icon_name']
