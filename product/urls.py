from rest_framework.routers import DefaultRouter
from django.urls import path, include
from product.api.views import ProductViewSet, CategoryViewSet

app_name = 'mainapp'

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('', include(router.urls)),
]
