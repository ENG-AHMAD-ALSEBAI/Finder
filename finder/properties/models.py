from django.db import models
from users.models import User

class Property(models.Model):
    CATEGORY_CHOICES = [
        ('rent', 'For Rent'),
        ('sale', 'For Sale'),
    ]
    
    PROPERTY_TYPE_CHOICES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('commercial', 'Commercial'),
        ('daily', 'Daily Rental'),
        ('new', 'New Building'),
    ]
    
    BUSINESS_TYPE_CHOICES = [
        ('business', 'I am a registered business'),
        ('private', 'I am a private seller'),
    ]

    STATUS_CHOICES = [
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]
    
    # Primary Key
    id_property = models.AutoField(primary_key=True)
    
    # Foreign Key to Custom User Model
    id_user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='properties', to_field='id_user', null=True, blank=True)
    
    # Basic Info Fields
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='rent')
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES, default='apartment')
    business_type = models.CharField(max_length=20, choices=BUSINESS_TYPE_CHOICES, default='private')
    pro_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.id_property}"

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

class PropertyLocation(models.Model):
    COUNTRY_CHOICES = [
        ('USA', 'United States'),
        ('UK', 'United Kingdom'),
        ('CA', 'Canada'),
    ]

    # Foreign Key to Property
    property = models.OneToOneField(Property, on_delete=models.CASCADE, primary_key=True)
    
    # Location Fields
    country = models.CharField(max_length=100, choices=COUNTRY_CHOICES, default='USA')
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    address = models.TextField()
    
    # Map Coordinates (اختياري)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

class PropertyDetails(models.Model):
    AMENITIES_CHOICES = [
        ('wifi', 'WiFi'),
        ('parking', 'Parking'),
        ('pool', 'Swimming Pool'),
        ('gym', 'Gym'),
        ('security', 'Security'),
        ('ac', 'Air Conditioning'),
        ('heating', 'Heating'),
        ('laundry', 'Laundry'),
        ('elevator', 'Elevator'),
        ('garden', 'Garden'),
    ]

    # Foreign Key to Property
    property = models.OneToOneField(Property, on_delete=models.CASCADE, primary_key=True)
    
    # Property Details Fields
    area = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField(default=1)
    bathrooms = models.IntegerField(default=1)
    parking = models.IntegerField(default=0)
    
    # Amenities as Multiple Choice
    amenities = models.CharField(
        max_length=255,
        choices=AMENITIES_CHOICES,
        default='wifi'
    )

    # Additional Details
    pets_allowed = models.BooleanField(default=False)
    description = models.TextField(blank=True)

class PropertyPrice(models.Model):
    CURRENCY_CHOICES = [
        ('USD', '$'),
        ('EUR', '€'),
        ('GBP', '£'),
        ('JPY', '¥'),
    ]
    
    PERIOD_CHOICES = [
        ('day', 'Per Day'),
        ('week', 'Per Week'),
        ('month', 'Per Month'),
        ('year', 'Per Year'),
    ]

    # Foreign Key to Property
    property = models.OneToOneField(Property, on_delete=models.CASCADE, primary_key=True)
    
    # Price Fields
    price = models.DecimalField(max_digits=12, decimal_places=2)
    price_currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='USD')
    price_period = models.CharField(max_length=10, choices=PERIOD_CHOICES, default='month')

class PropertyPhoto(models.Model):
    # Foreign Key to Property
    property = models.OneToOneField(Property, on_delete=models.CASCADE, primary_key=True)
    
    # Photo Fields
    main_photo = models.ImageField(upload_to='properties/main/')
    photo_1 = models.ImageField(upload_to='properties/additional/', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='properties/additional/', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='properties/additional/', blank=True, null=True)

class PropertyContacts(models.Model):
    # Foreign Key to Property
    property = models.OneToOneField(Property, on_delete=models.CASCADE, primary_key=True)
    
    # Contact Fields
    contact_name = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=20)
    contact_email = models.EmailField()
    company_name = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'Property Contact'
        verbose_name_plural = 'Property Contacts'
