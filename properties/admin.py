from django.contrib import admin
from .models import (
    Property, 
    PropertyLocation, 
    PropertyDetails, 
    PropertyPrice, 
    PropertyPhoto, 
    PropertyContacts
)

class PropertyLocationInline(admin.StackedInline):
    model = PropertyLocation
    can_delete = False
    verbose_name_plural = 'Location Information'

class PropertyDetailsInline(admin.StackedInline):
    model = PropertyDetails
    can_delete = False
    verbose_name_plural = 'Property Details'

class PropertyPriceInline(admin.StackedInline):
    model = PropertyPrice
    can_delete = False
    verbose_name_plural = 'Price Information'

class PropertyPhotoInline(admin.StackedInline):
    model = PropertyPhoto
    can_delete = False
    verbose_name_plural = 'Property Photos'

class PropertyContactsInline(admin.StackedInline):
    model = PropertyContacts
    can_delete = False
    verbose_name_plural = 'Contact Information'

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'id_user', 'property_type', 'category', 'pro_status', 'created_at')
    list_filter = ('property_type', 'category', 'pro_status')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    
    inlines = [
        PropertyLocationInline,
        PropertyDetailsInline,
        PropertyPriceInline,
        PropertyPhotoInline,
        PropertyContactsInline
    ]

    def has_change_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True

    fieldsets = (
        ('Basic Information', {
            'fields': (
                'id_user',
                'title',
                'category',
                'property_type',
                'business_type',
                'pro_status'
            )
        }),
    )

@admin.register(PropertyLocation)
class PropertyLocationAdmin(admin.ModelAdmin):
    list_display = ('property', 'country', 'city', 'district', 'zip_code')
    list_filter = ('country', 'city')
    search_fields = ('address', 'city', 'district')

@admin.register(PropertyDetails)
class PropertyDetailsAdmin(admin.ModelAdmin):
    list_display = ('property', 'area', 'bedrooms', 'bathrooms', 'parking', 'pets_allowed', 'amenities')
    list_filter = ('pets_allowed', 'bedrooms', 'bathrooms', 'amenities')
    search_fields = ('description',)

@admin.register(PropertyPrice)
class PropertyPriceAdmin(admin.ModelAdmin):
    list_display = ('property', 'price', 'price_currency', 'price_period')
    list_filter = ('price_currency', 'price_period')
    search_fields = ('price',)

@admin.register(PropertyPhoto)
class PropertyPhotoAdmin(admin.ModelAdmin):
    list_display = ('property', 'main_photo', 'photo_1', 'photo_2', 'photo_3')
    search_fields = ('property__title',)

@admin.register(PropertyContacts)
class PropertyContactsAdmin(admin.ModelAdmin):
    list_display = ('property', 'contact_name', 'contact_phone', 'contact_email', 'company_name')
    search_fields = ('contact_name', 'contact_email', 'company_name')
