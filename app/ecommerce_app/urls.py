"""
URL configuration for ecommerce_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)


schema_view = get_schema_view(
    openapi.Info(
        title="E-Commerce Backend API",
        default_version='v1',
        description="""
        This API is part of a backend system developed as a specialization thesis project.
        It provides core functionality for e-commerce platforms, including user authentication, product and cart management, order processing, and payment integration.

        Built with Django and Django REST Framework, the API is designed to be lightweight, scalable, and easy to use — especially for students and small teams who need a clean and minimal alternative to complex systems like Saleor or Oscar.

        Main features:
        - JWT-based authentication and role-based access
        - CRUD for products, categories, carts, and orders
        - Stripe payment and webhook support
        - Image handling with Cloudinary
        - Dockerized deployment, hosted on AWS
        """,
        contact=openapi.Contact(email="napsatarov@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls', namespace='mainapp')),
    path('', include('cart.urls', namespace='cart')),
    path('', include('checkout.urls', namespace='checkout')),

    path('auth/', include('dj_rest_auth.urls')),  # login/logout/password
    path('auth/registration/', include('dj_rest_auth.registration.urls')),  # registration
    path('accounts/', include('allauth.urls')),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]  # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
