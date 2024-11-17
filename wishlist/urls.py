from django.urls import path , include
from . import views

urlpatterns = [
    path('account_wishlist/', views.account_wishlist, name='account_wishlist'),
]
