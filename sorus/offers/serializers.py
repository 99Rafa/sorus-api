from rest_framework import serializers

from offers.models import Review


class CreateReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['date', 'rate', 'title', 'comment', 'product', 'user']
