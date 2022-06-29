from django.urls import path
from .views import index, cart, products, removecart,products,success_page, error_page

urlpatterns = [
    path('', index),
    path('cart/', cart),
    path('cart/remove/<int:id>', removecart),
    path('product/', products),
    path('success_page/', success_page, name="success_page"),
    path('error_page/', error_page, name="error_page"),
]