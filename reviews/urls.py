from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('vendor_reviews/', views.vendor_reviews , name='vendor_reviews'),
    path('account_reviews/', views.account_reviews, name='account_reviews'),
    path('vendor_properties/', views.vendor_properties, name='vendor_properties'),
    

]

