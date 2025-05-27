from rest_framework import serializers

from myapi.models import Category, Product, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"