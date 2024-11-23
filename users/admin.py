from django.contrib import admin
from .models import User, UserInfo

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

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    # القائمة التي تظهر في صفحة عرض معلومات المستخدمين
    list_display = ('user', 'company_name', 'address')
    
    # حقول البحث
    search_fields = ('user__full_name', 'user__email', 'company_name', 'address')
    
    # ترتيب الحقول في صفحة التفاصيل
    fieldsets = (
        ('المعلومات الأساسية', {
            'fields': ('user', 'short_bio', 'company_name', 'address')
        }),
        ('روابط التواصل الاجتماعي', {
            'fields': ('facebook', 'linkedin', 'twitter', 'instagram'),
            'classes': ('collapse',)  # قابلة للطي
        }),
    )
    
    # عدد العناصر في الصفحة
    list_per_page = 25
    
    # العلاقة مع المستخدم
    autocomplete_fields = ['user']
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # في حالة التعديل
            return ('user',)  # لا يمكن تغيير المستخدم بعد الإنشاء
        return ()
