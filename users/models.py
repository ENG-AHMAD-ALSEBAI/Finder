from django.db import models

class User(models.Model):
    id_user = models.AutoField(primary_key=True)  # Primary Key with custom name
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    type_subscribe = models.CharField(max_length=50)  # e.g., Free, Premium
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)

    def __str__(self):
        return self.full_name
    
    def get_photo_url(self):
        if self.photo:
            return self.photo.url
        return None

class UserInfo(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='info',
        primary_key=True  # جعل حقل user هو المفتاح الرئيسي
    )
    short_bio = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=50, blank=True, null=True)
    linkedin = models.CharField(max_length=50, blank=True, null=True)
    twitter = models.CharField(max_length=50, blank=True, null=True)
    instagram = models.CharField(max_length=50, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"معلومات {self.user.full_name}"

    class Meta:
        verbose_name = "معلومات المستخدم"
        verbose_name_plural = "معلومات المستخدمين"

    
