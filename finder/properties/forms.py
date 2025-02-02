from django import forms
from .models import Property, PropertyLocation, PropertyDetails, PropertyPrice, PropertyPhoto, PropertyContacts

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'category', 'property_type', 'business_type', 'pro_status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter property title'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'property_type': forms.Select(attrs={'class': 'form-select'}),
            'business_type': forms.RadioSelect(attrs={
                'class': 'form-check-input me-1',
                'style': 'margin-right: 10px;'
            }),
            'pro_status': forms.Select(attrs={'class': 'form-select'})
        }

class PropertyLocationForm(forms.ModelForm):
    class Meta:
        model = PropertyLocation
        fields = ['country', 'city', 'district', 'zip_code', 'address', 'latitude', 'longitude']
        widgets = {
            'country': forms.Select(attrs={'class': 'form-select'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter district'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter zip code'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter full address'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control'})
        }

class PropertyDetailsForm(forms.ModelForm):
    amenities = forms.MultipleChoiceField(
        choices=PropertyDetails.AMENITIES_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-check-input me-1'
        }),
        required=False
    )

    class Meta:
        model = PropertyDetails
        fields = ['area', 'bedrooms', 'bathrooms', 'parking', 'amenities', 'pets_allowed', 'description']
        widgets = {
            'area': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter area in sq.m'}),
            'bedrooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'bathrooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'parking': forms.NumberInput(attrs={'class': 'form-control'}),
            'pets_allowed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
        }

class PropertyPriceForm(forms.ModelForm):
    class Meta:
        model = PropertyPrice
        fields = ['price', 'price_currency', 'price_period']
        widgets = {
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'price_currency': forms.Select(attrs={'class': 'form-select'}),
            'price_period': forms.Select(attrs={'class': 'form-select'})
        }

class PropertyPhotoForm(forms.ModelForm):
    class Meta:
        model = PropertyPhoto
        fields = ['main_photo', 'photo_1', 'photo_2', 'photo_3']
        widgets = {
            'main_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'photo_1': forms.FileInput(attrs={'class': 'form-control'}),
            'photo_2': forms.FileInput(attrs={'class': 'form-control'}),
            'photo_3': forms.FileInput(attrs={'class': 'form-control'})
        }

class PropertyContactsForm(forms.ModelForm):
    class Meta:
        model = PropertyContacts
        fields = ['contact_name', 'contact_phone', 'contact_email', 'company_name']
        widgets = {
            'contact_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contact name'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter company name (optional)'})
        }
