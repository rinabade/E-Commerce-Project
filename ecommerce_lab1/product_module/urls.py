from django.urls import path
from .views import index, cart, products, removecart,products
urlpatterns = [
    path('', index),
    path('cart/', cart),
    path('cart/remove/<int:id>', removecart),
    path('product/', products),
]