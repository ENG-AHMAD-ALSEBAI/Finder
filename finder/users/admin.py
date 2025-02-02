from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserInfo

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'full_name', 'type_subscribe', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff', 'type_subscribe')
    search_fields = ('email', 'full_name')
    ordering = ('email',)
    
    fieldsets = (
        ('Account Information', {'fields': ('email', 'password')}),
        ('Personal Information', {'fields': ('full_name', 'first_name', 'last_name', 'phone_number', 'photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'type_subscribe')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2'),
        }),
    )

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'address')
    search_fields = ('user__email', 'company_name')

admin.site.register(User, CustomUserAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
