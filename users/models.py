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
