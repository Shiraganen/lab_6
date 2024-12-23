from rest_framework import serializers
from .models import Category, Coffee, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
