from django.shortcuts import render

# Create your views here.
def single_v2(requste):
   return render(requste , 'real-estate-single-v2')

def single_v1(requste):
   return render(requste , 'real-estate-single-v1')

def property_promotion(requste):
   return render(requste , 'real-estate-property-promotion.html')

def home(requste):
   return render(requste , 'real-estate-home-v1.html')

def catalog_sale(requste):
   return render(requste , 'real-estate-catalog-sale.html')

def catalog_rent(requste):
   return render(requste , 'real-estate-catalog-rent.html') 
 
def add_property(requste):
   return render(requste , 'real-estate-add-property.html')  

def account_properties(requste):
   return render(requste , 'real-estate-account-properties.html')    

def vendor_properties(requste):
   return render(requste , 'real-estate-vendor-properties.html')      
