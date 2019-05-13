from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

# Right Now Only Using fields provided in User Model. Profile Model Template For Future

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shopOwner = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
# 	instance.profile.save()