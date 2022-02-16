from django.urls import path
from . import views

app_name    = "shop"
urlpatterns = [
    path('', views.index, name="index"),
    path('<uuid:pk>/', views.product, name="product"),
    path('cart/', views.cart, name="cart"),
]

