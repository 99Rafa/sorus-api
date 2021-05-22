from rest_framework import serializers

from users.models import User


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'profile_image', 'password']


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password', 'state', 'user_type']
