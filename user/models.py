from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30, unique=True)
    bio = models.TextField(blank=True, default='')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, default='/profile_pictures/default.jpg')

    def save(self, *args, **kwargs):
        self.username = self.user.username
        super().save(*args, **kwargs)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)