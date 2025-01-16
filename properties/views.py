from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import (
    PropertyForm, PropertyLocationForm, PropertyDetailsForm,
    PropertyPriceForm, PropertyPhotoForm, PropertyContactsForm
)
from .models import Property
from users.models import User  # إضافة استيراد نموذج المستخدم المخصص

@login_required
def add_property(request):
    if request.method == 'POST':
        try:
            property_form = PropertyForm(request.POST)
            location_form = PropertyLocationForm(request.POST)
            details_form = PropertyDetailsForm(request.POST)
            price_form = PropertyPriceForm(request.POST)
            photo_form = PropertyPhotoForm(request.POST, request.FILES)
            contacts_form = PropertyContactsForm(request.POST)

            forms = [
                property_form, location_form, details_form,
                price_form, photo_form, contacts_form
            ]

            if all(form.is_valid() for form in forms):
                try:
                    # Get the user
                    user = User.objects.get(email=request.user.email)
                    
                    # Create property instance but don't save yet
                    property_instance = property_form.save(commit=False)
                    property_instance.id_user = user
                    property_instance.save()

                    # Save location
                    location = location_form.save(commit=False)
                    location.property = property_instance
                    location.save()

                    # Save details
                    details = details_form.save(commit=False)
                    details.property = property_instance
                    details.amenities = details_form.cleaned_data.get('amenities', '')
                    details.save()

                    # Save price
                    price = price_form.save(commit=False)
                    price.property = property_instance
                    price.save()

                    # Save photos
                    photo = photo_form.save(commit=False)
                    photo.property = property_instance
                    photo.save()

                    # Save contact
                    contacts = contacts_form.save(commit=False)
                    contacts.property = property_instance
                    contacts.save()

                    messages.success(request, 'Property added successfully!')
                    return redirect('properties:account_properties')
                except User.DoesNotExist:
                    messages.error(request, 'User not found. Please make sure you are logged in.')
                except Exception as e:
                    messages.error(request, f'Error saving property: {str(e)}')
            else:
                for form in forms:
                    for field, errors in form.errors.items():
                        for error in errors:
                            messages.error(request, f'{field}: {error}')
        except Exception as e:
            messages.error(request, f'Unexpected error: {str(e)}')

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

def single_v1(request, property_id):
    if request.method == 'POST' and 'delete_property' in request.POST:
        try:
            # البحث عن الملكية باستخدام المستخدم المخصص ومعرف الملكية
            property = Property.objects.get(id_user=custom_user, id_property=property_id)
            property.delete()
            messages.success(request, 'Property deleted successfully')
            return redirect('properties:account_properties')
        except Property.DoesNotExist:
            messages.error(request, 'Property not found')
            return redirect('properties:account_properties')
        except User.DoesNotExist:
            messages.error(request, 'User not found')
            return redirect('properties:account_properties')
    
    try:
        # الحصول على المستخدم المخصص
        custom_user = User.objects.get(email=request.user.email)
        # Get the property with all related data
        property = Property.objects.select_related(
            'propertylocation',
            'propertydetails',
            'propertyprice',
            'propertyphoto',
            'id_user'  # إضافة علاقة المستخدم
        ).get(id_property=property_id)
        
        context = {
            'property': property,
            'user': custom_user  # إضافة المستخدم إلى السياق
        }
        return render(request, 'real-estate-single-v1.html', context)
    except Property.DoesNotExist:
        messages.error(request, 'Property not found')
        return redirect('properties:account_properties')

def property_promotion(request):
   return render(request , 'real-estate-property-promotion.html')

def home(request):
    # Get featured properties
    properties = Property.objects.select_related(
        'propertylocation',
        'propertydetails',
        'propertyprice',
        'propertyphoto'
    ).all()[:8]  # Get first 8 properties
    
    context = {
        'properties': properties
    }
    return render(request, 'real-estate-home-v1.html', context)

def catalog_sale(request):
    try:
        # الحصول على جميع الملكيات المنشورة للإيجار
        properties = Property.objects.filter(
            pro_status='published',  # تغيير من Published إلى published
            category='sale'  # تغيير من For Sale إلى sale
        ).select_related(
            'propertylocation',
            'propertydetails',
            'propertyprice',
            'propertyphoto'
        )

        # طباعة معلومات التصحيح للتأكد
        print("=== بداية معلومات التصحيح ===")
        print("عدد الملكيات المعروضة:", properties.count())
        
        context = {
            'properties': properties
        }
        return render(request, 'real-estate-catalog-sale.html', context)
        
    except Exception as e:
        print("حدث خطأ:", str(e))
        return render(request, 'real-estate-catalog-sale.html', {'properties': []})


def catalog_rent(request):
    try:
        # الحصول على جميع الملكيات المنشورة للإيجار
        properties = Property.objects.filter(
            pro_status='published',  # تغيير من Published إلى published
            category='rent'  # تغيير من For Rent إلى rent
        ).select_related(
            'propertylocation',
            'propertydetails',
            'propertyprice',
            'propertyphoto'
        )

        # طباعة معلومات التصحيح للتأكد
        print("=== بداية معلومات التصحيح ===")
        print("عدد الملكيات المعروضة:", properties.count())
        
        context = {
            'properties': properties
        }
        return render(request, 'real-estate-catalog-rent.html', context)
        
    except Exception as e:
        print("حدث خطأ:", str(e))
        return render(request, 'real-estate-catalog-rent.html', {'properties': []})

@login_required
def account_properties(request):
    try:
        # الحصول على المستخدم المخصص
        custom_user = User.objects.get(email=request.user.email)
        
        # التحقق من طلب حذف جميع الملكيات
        if request.method == 'POST' and 'delete_all' in request.POST:
            try:
                # حذف جميع الملكيات للمستخدم
                Property.objects.filter(id_user=custom_user).delete()
                messages.success(request, 'All properties have been deleted successfully')
                return redirect('properties:account_properties')
            except Exception as e:
                messages.error(request, 'An error occurred while deleting properties')
                return redirect('properties:account_properties')
        
        # الحصول على جميع الملكيات المنشورة للمستخدم
        properties = Property.objects.filter(
            id_user=custom_user,
            pro_status='published'
        ).select_related(
            'propertylocation',
            'propertydetails',
            'propertyprice',
            'propertyphoto'
        )
        
        context = {
            'properties': properties,
            'user': custom_user
        }
        return render(request, 'real-estate-account-properties.html', context)
        
    except User.DoesNotExist:
        messages.error(request, 'User not found')
        return redirect('users:signin')

@login_required
def account_properties_archived(request):
    try:
        # الحصول على المستخدم المخصص
        custom_user = User.objects.get(email=request.user.email)
        
        # التحقق من طلب حذف جميع الملكيات
        if request.method == 'POST' and 'delete_all' in request.POST:
            try:
                # حذف جميع الملكيات المؤرشفة للمستخدم
                Property.objects.filter(
                    id_user=custom_user,
                    pro_status='archived'
                ).delete()
                messages.success(request, 'All archived properties have been deleted successfully')
                return redirect('properties:account_properties_archived')
            except Exception as e:
                messages.error(request, 'An error occurred while deleting properties')
                return redirect('properties:account_properties_archived')
        
        # الحصول على جميع الملكيات المؤرشفة للمستخدم
        properties = Property.objects.filter(
            id_user=custom_user,
            pro_status='archived'
        ).select_related(
            'propertylocation',
            'propertydetails',
            'propertyprice',
            'propertyphoto'
        )
        
        context = {
            'properties': properties,
            'user': custom_user
        }
        return render(request, 'real-estate-account-properties_archived.html', context)
        
    except User.DoesNotExist:
        messages.error(request, 'User not found')
        return redirect('users:signin')

@login_required
def publish_archived_property(request, property_id=None):
    if request.method == 'POST':
        if property_id:
            try:
                # Publish single property
                property = Property.objects.get(id_property=property_id)
                # التحقق من أن المستخدم هو المالك أو مشرف
                if request.user.is_superuser or property.id_user == request.user:
                    if property.pro_status == 'archived':
                        property.pro_status = 'published'
                        property.save()
                        messages.success(request, 'Property has been published successfully.')
                        return redirect('properties:account_properties_archived')
                    else:
                        messages.info(request, 'Property is already published.')
                else:
                    messages.error(request, 'You do not have permission to publish this property.')
            except Property.DoesNotExist:
                messages.error(request, 'Property not found.')
        else:
            # Publish all archived properties
            if request.user.is_superuser:
                properties = Property.objects.filter(pro_status='archived')
            else:
                properties = Property.objects.filter(id_user=request.user, pro_status='archived')
            
            count = properties.count()
            if count > 0:
                properties.update(pro_status='published')
                messages.success(request, f'{count} properties have been published successfully.')
            else:
                messages.info(request, 'No archived properties found.')
    
    if property_id:
        return redirect('properties:single_v1', property_id=property_id)
    return redirect('properties:account_properties_archived')

@login_required
def delete_property(request, property_id):
    try:
        property = Property.objects.get(id=property_id)
        # التحقق من أن المستخدم هو مالك الملكية
        if property.id_user == request.user:
            property.delete()
            messages.success(request, 'Property deleted successfully')
        else:
            messages.error(request, 'You do not have permission to delete this property')
    except Property.DoesNotExist:
        messages.error(request, 'Property not found')
    
    return redirect('properties:account_properties')

@login_required
def delete_all_properties(request):
    if request.method == 'POST':
        try:
            # الحصول على المستخدم المخصص
            custom_user = User.objects.get(email=request.user.email)
            # حذف جميع الملكيات للمستخدم
            Property.objects.filter(id_user=custom_user).delete()
            messages.success(request, 'All properties have been deleted successfully')
        except User.DoesNotExist:
            messages.error(request, 'User not found')
        except Exception as e:
            messages.error(request, 'An error occurred while deleting properties')
    
    return redirect('properties:account_properties')

def vendor_properties(request):
   return render(request , 'real-estate-vendor-properties.html')      