from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ProductViewSet, register_user, CustomLoginView

# Set up REST Framework router for ProductViewSet
router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    # Regular HTML views
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('contact/', views.contact, name='contact'),

    # Cart
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    # Wishlist
    path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', views.view_wishlist, name='view_wishlist'),

    # HTML Register/Login/Logout Pages
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Function-based product API
    path('product-list/', views.product_api, name='product_api'),

    # DRF ViewSet routes
    path('api/', include(router.urls)),

    # Auth API endpoints
    path('api/register/', register_user, name='api_register'),
    path('api/login/', CustomLoginView.as_view(), name='api_login'),
]
