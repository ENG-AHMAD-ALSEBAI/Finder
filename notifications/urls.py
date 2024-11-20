from django.urls import path, include
from . import views

app_name = 'notifications'

urlpatterns = [
    path('account_notifications/', views.account_notifications, name='account_notifications'),
]

