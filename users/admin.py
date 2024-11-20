from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # القائمة التي تظهر في صفحة عرض المستخدمين
    list_display = ('id_user', 'full_name', 'email', 'phone_number', 'type_subscribe')
    
    # حقول البحث
    search_fields = ('email', 'phone_number', 'first_name', 'last_name', 'full_name')
    
    # الفلترة في الجانب
    list_filter = ('type_subscribe',)
    
    # ترتيب الحقول في صفحة التفاصيل
    fieldsets = (
        ('معلومات الحساب', {
            'fields': ('email', 'password', 'type_subscribe')
        }),
        ('المعلومات الشخصية', {
            'fields': ('first_name', 'last_name', 'full_name', 'phone_number', 'photo')
        }),
    )
    
    # الحقول التي يمكن تعديلها في صفحة القائمة مباشرة
    list_editable = ('type_subscribe',)
    
    # عدد العناصر في الصفحة
    list_per_page = 25
    
    # إضافة رابط للصورة في صفحة التفاصيل
    readonly_fields = ('get_photo_preview',)
    
    def get_photo_preview(self, obj):
        if obj.photo:
            return f'<img src="{obj.photo.url}" width="150" height="150" />'
        return 'لا توجد صورة'
    get_photo_preview.short_description = 'معاينة الصورة'
    get_photo_preview.allow_tags = True
