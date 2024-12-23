from rest_framework import viewsets, permissions
from .models import Category, Coffee, Order
from .serializers import CategorySerializer, CoffeeSerializer, OrderSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class CoffeeViewSet(viewsets.ModelViewSet):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
