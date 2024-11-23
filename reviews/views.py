from django.shortcuts import render
name = 'reviews'
# Create your views here.
def vendor_reviews(requste):
   return render(requste , 'real-estate-vendor-reviews.html')

def vendor_properties(requste):
   return render(requste , 'real-estate-vendor-properties.html')

def account_reviews(requste):
   return render(requste , 'real-estate-account-reviews.html')
