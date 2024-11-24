from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import (
    PropertyForm, PropertyLocationForm, PropertyDetailsForm,
    PropertyPriceForm, PropertyPhotoForm, PropertyContactsForm
)

@login_required
def add_property(request):
    if request.method == 'POST':
        property_form = PropertyForm(request.POST)
        location_form = PropertyLocationForm(request.POST)
        details_form = PropertyDetailsForm(request.POST)
        price_form = PropertyPriceForm(request.POST)
        photo_form = PropertyPhotoForm(request.POST, request.FILES)
        contacts_form = PropertyContactsForm(request.POST)

        if all([property_form.is_valid(), location_form.is_valid(),
               details_form.is_valid(), price_form.is_valid(),
               photo_form.is_valid(), contacts_form.is_valid()]):
            
            # حفظ النموذج الرئيسي أولاً
            property = property_form.save(commit=False)
            property.id_user = request.user
            property.save()

            # حفظ النماذج المرتبطة
            location = location_form.save(commit=False)
            location.property = property
            location.save()

            details = details_form.save(commit=False)
            details.property = property
            details.amenities = details_form.cleaned_data['amenities']
            details.save()

            price = price_form.save(commit=False)
            price.property = property
            price.save()

            photo = photo_form.save(commit=False)
            photo.property = property
            photo.save()

            contacts = contacts_form.save(commit=False)
            contacts.property = property
            contacts.save()

            return redirect('properties:property_promotion')
    else:
        property_form = PropertyForm()
        location_form = PropertyLocationForm()
        details_form = PropertyDetailsForm()
        price_form = PropertyPriceForm()
        photo_form = PropertyPhotoForm()
        contacts_form = PropertyContactsForm()

    context = {
        'property_form': property_form,
        'location_form': location_form,
        'details_form': details_form,
        'price_form': price_form,
        'photo_form': photo_form,
        'contacts_form': contacts_form,
    }
    
    return render(request, 'real-estate-add-property.html', context)

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
 
def account_properties(requste):
   return render(requste , 'real-estate-account-properties.html')    

def vendor_properties(requste):
   return render(requste , 'real-estate-vendor-properties.html')      
