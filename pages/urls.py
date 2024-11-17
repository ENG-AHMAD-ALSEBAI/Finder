from django.urls import path , include
from . import views

urlpatterns = [
    path('signup/', views.signup , name='signup'),
    
    path('signin/', views.signin , name='signin'),
    
    path('vendor_reviews/', views.vendor_reviews , name='vendor_reviews'),

    path('vendor_properties/', views.vendor_properties , name='vendor_properties'),

    path('single_v1/', views.single_v1 , name='single_v1'),

    path('single_v2/', views.single_v2 , name='single_v2'),

    path('property_promotion/', views.property_promotion , name='property_promotion'),

    path('home/', views.home, name='home'),

    path('help_center/', views.help_center, name='help_center'),

    path('contacts/', views.contacts, name='contacts'),

    path('catalog_sale/', views.catalog_sale, name='catalog_sale'),

    path('catalog_rent/', views.catalog_rent, name='catalog_rent'),

    path('blog/', views.blog, name='blog'),

    path('blog_single/', views.blog_single, name='blog_single'),

    path('add_property/', views.add_property, name='add_property'),

    path('account_wishlist/', views.account_wishlist, name='account_wishlist'),

    path('account_security/', views.account_security, name='account_security'),

    path('account_reviews/', views.account_reviews, name='account_reviews'),

    path('account_properties/', views.account_properties, name='account_properties'),

    path('account_notifications/', views.account_notifications, name='account_notifications'),

    path('account_info/', views.account_info, name='account_info'),

    path('about/', views.about, name='about'),
    
    path('account_404/', views.error_404, name='account_404'),

    path('navbar/', views.navbar, name='navbar'),
]
