from django.shortcuts import render
from django.http import HttpResponse

def signin(requste):
   return render(requste , 'signin-light.html')

def signup(requste):
   return render(requste , 'signup-light.html')

def vendor_reviews(requste):
   return render(requste , 'real-estate-vendor-reviews.html')

def vendor_properties(requste):
   return render(requste , 'real-estate-vendor-properties.html')

def single_v2(requste):
   return render(requste , 'real-estate-single-v2')

def single_v1(requste):
   return render(requste , 'real-estate-single-v1')

def property_promotion(requste):
   return render(requste , 'real-estate-property-promotion.html')

def home(request):
   return render(request, 'real-estate-home-v1.html')

def help_center(requste):
   return render(requste , 'real-estate-help-center.html')

def contacts(requste):
   return render(requste , 'real-estate-contacts.html')

def catalog_sale(requste):
   return render(requste , 'real-estate-catalog-sale.html')

def catalog_rent(requste):
   return render(requste , 'real-estate-catalog-rent.html')

def blog(requste):
   return render(requste , 'real-estate-blog.html')

def blog_single(requste):
   return render(requste , 'real-estate-blog-single.html')

def add_property(requste):
   return render(requste , 'real-estate-add-property.html')

def account_wishlist(requste):
   return render(requste , 'real-estate-account-wishlist.html')

def account_security(requste):
   return render(requste , 'real-estate-account-security.html')

def account_reviews(requste):
   return render(requste , 'real-estate-account-reviews.html')

def account_properties(requste):
   return render(requste , 'real-estate-account-properties.html')

def account_notifications(requste):
   return render(requste , 'real-estate-account-notifications.html')

def account_info(requste):
   return render(requste , 'real-estate-account-info.html')

def about(requste):
   return render(requste , 'real-estate-about.html')

def error_404(requste):
   return render(requste , 'real-estate-404.html')

def navbar(requste):
   return render(requste , 'navbar.html')