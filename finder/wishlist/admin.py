from django.contrib import admin
from .models import WishlistItem

# Register your models here.

@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'property', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__full_name', 'user__email', 'property__title']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    raw_id_fields = ['user', 'property']
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user', 'property')
