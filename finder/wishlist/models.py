from django.db import models
from users.models import User
from properties.models import Property
from django.utils import timezone

# Create your models here.

class WishlistItem(models.Model):
    id_wishlist = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='wishlist_items',
        to_field='id_user'
    )
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='in_wishlists',
        to_field='id_property'
    )
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        # لضمان عدم تكرار نفس العقار في قائمة المفضلة للمستخدم الواحد
        unique_together = ['user', 'property']
        # ترتيب العناصر من الأحدث إلى الأقدم
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.full_name} - {self.property.title}"
