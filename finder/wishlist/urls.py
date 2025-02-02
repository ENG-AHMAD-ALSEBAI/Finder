from django.urls import path
from . import views

app_name = 'wishlist'

urlpatterns = [
    path('account_wishlist/', views.account_wishlist, name='account_wishlist'),
    path('', views.wishlist, name='wishlist'),
    path('toggle/', views.toggle_wishlist, name='toggle_wishlist'),
    path('clear/', views.clear_wishlist, name='clear_wishlist'),
]