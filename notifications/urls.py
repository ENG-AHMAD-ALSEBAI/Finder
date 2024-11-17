from django.urls import path , include
from . import views

urlpatterns = [
    path('account_notifications/', views.account_notifications, name='account_notifications'),
]

