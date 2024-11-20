from django.urls import path, include
from . import views

app_name = 'wishlist'

urlpatterns = [
    path('account_wishlist/', views.account_wishlist, name='account_wishlist'),
]
