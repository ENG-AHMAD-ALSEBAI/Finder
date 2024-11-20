from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('security/', views.account_security, name='security'),
    path('account_info/', views.account_info, name='account_info'),
    path('account_notifications/', views.account_notifications, name='account_notifications'),
]

