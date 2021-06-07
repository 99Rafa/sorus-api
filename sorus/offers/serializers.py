from rest_framework import serializers

from offers.models import Product, Review, Category
from users.models import User


class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['rate', 'title', 'comment', 'product', 'user']


class ListReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['rate', 'title', 'comment']


class CreateOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'start_date', 'end_date',
                  'promoter', 'state', 'category', 'stock', 'is_offer']


class UserStarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['stars']


class ListOfferSerializer(serializers.ModelSerializer):
    promoter = UserStarsSerializer(many=False, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'stock', 'is_offer',
                  'start_date', 'end_date', 'time_left', 'still_active', 'category', 'promoter']


class UpdateOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image',
                  'end_date', 'category', 'stock', 'is_offer']


class ListCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'icon_name']
