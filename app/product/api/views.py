from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.permissions import AllowAny, IsAdminUser

from product.api.serializers import ProductSerializer, CategorySerializer
from product.filters import ProductFilter
from product.models import Product, Category


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('name', openapi.IN_QUERY, description="Search by product name", type=openapi.TYPE_STRING),
        openapi.Parameter('price_min', openapi.IN_QUERY, description="Minimum price", type=openapi.TYPE_INTEGER),
        openapi.Parameter('price_max', openapi.IN_QUERY, description="Maximum price", type=openapi.TYPE_INTEGER),
        openapi.Parameter('category', openapi.IN_QUERY, description="Filter by category id", type=openapi.TYPE_INTEGER),
    ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
