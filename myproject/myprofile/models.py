from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from django.utils import timezone
import requests
# Create your models here

class profiles(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, )
    numOfFollowers = models.IntegerField(default = 0)
    lastUpdated = models.DateTimeField(auto_now=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            profiles.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profiles.save()

class repository(models.Model):
    profiles = models.ForeignKey(profiles, on_delete = models.CASCADE)
    name = models.CharField(max_length=30)
    stars = models.IntegerField(default = 0)

    class Meta:
        ordering = ['-stars']