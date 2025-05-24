from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    age = models.PositiveBigIntegerField(null=True, blank=True)
    image = models.ImageField(
        upload_to='profile_images', null=True, blank=True
    )
    user =models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile'
    )

    def __str__(self):
        return f'{self.user.username} Profile'
    
    class Meta:
        verbose_name = 'Profile'
        db_table = 'user_profile'