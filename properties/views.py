from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import (
    PropertyForm, PropertyLocationForm, PropertyDetailsForm,
    PropertyPriceForm, PropertyPhotoForm, PropertyContactsForm
)
from .models import Property
from users.models import User  # إضافة استيراد نموذج المستخدم المخصص

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

def single_v2(request):
   return render(request , 'real-estate-single-v2')

def single_v1(request):
    try:
        # Get the custom user
        custom_user = User.objects.get(email=request.user.email)
        # Get the property with all related data
        property = Property.objects.select_related(
            'propertylocation',
            'propertydetails',
            'propertyprice',
            'propertyphoto',
            'propertycontacts'
        ).first()  # Get the first property for now
        
        context = {
            'property': property,
            'user': custom_user,
        }
        return render(request, 'real-estate-single-v1.html', context)
    except Property.DoesNotExist:
        return redirect('properties:catalog_rent')

def property_promotion(request):
   return render(request , 'real-estate-property-promotion.html')

def home(request):
   return render(request , 'real-estate-home-v1.html')

def catalog_sale(request):
   return render(request , 'real-estate-catalog-sale.html')

def catalog_rent(request):
   return render(request , 'real-estate-catalog-rent.html') 
 
@login_required
def account_properties(request):
    try:
        # Get the custom user
        custom_user = User.objects.get(email=request.user.email)
        # Get the user's properties with all related data
        properties = Property.objects.filter(id_user=custom_user).select_related(
            'propertylocation',
            'propertydetails',
            'propertyprice',
            'propertyphoto',
            'propertycontacts'
        )
        context = {
            'user': custom_user,
            'properties': properties
        }
        return render(request, 'real-estate-account-properties.html', context)
    except User.DoesNotExist:
        return redirect('login')

def vendor_properties(requste):
   return render(requste , 'real-estate-vendor-properties.html')      
