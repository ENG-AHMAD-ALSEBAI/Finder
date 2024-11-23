from django.urls import path , include
from . import views

app_name = 'properties'

urlpatterns = [
    
    path('single_v1/', views.single_v1 , name='single_v1'),
    path('single_v2/', views.single_v2 , name='single_v2'),
    path('property_promotion/', views.property_promotion , name='property_promotion'),
    path('home/', views.home, name='home'),
    path('catalog_sale/', views.catalog_sale, name='catalog_sale'),
    path('catalog_rent/', views.catalog_rent, name='catalog_rent'),
    path('add_property/', views.add_property, name='add_property'),
    path('account_properties/', views.account_properties, name='account_properties'),
    path('vendor_properties/', views.vendor_properties, name='vendor_properties'),
]

