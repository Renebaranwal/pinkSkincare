from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# 🔹 Product Serializer (for products API)
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# 🔹 User Register Serializer (for user signup API)
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
