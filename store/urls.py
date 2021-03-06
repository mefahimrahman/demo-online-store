from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('updateItem/', views.update_item, name='updateItem'),
    path('processOrder/', views.process_order, name='processOrder'),
]