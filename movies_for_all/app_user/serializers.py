from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import AppUser


class UserSerializer(serializers.Serializer):

    """
        User model serializer
    """

    username = serializers.CharField(max_length=100, validators=[UniqueValidator(
        queryset=AppUser.objects.all())])
    password = serializers.CharField(max_length=100)
    first_name = serializers.CharField(max_length=30, required=False)
    last_name = serializers.CharField(max_length=30, required=False)
    email = serializers.EmailField(max_length=100, validators=[UniqueValidator(
        queryset=AppUser.objects.all())])
    is_staff = serializers.BooleanField(required=False)
    is_active = serializers.BooleanField(required=False)
    is_subscribed = serializers.BooleanField(required=False)

    def create(self, validated_data):
        user = AppUser.objects.create_user(**validated_data)
        return user
