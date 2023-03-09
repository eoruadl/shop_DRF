from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from phonenumber_field.modelfields import PhoneNumberField

class Address(models.Model):
    postal_code = models.CharField(max_length=6)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    street_address = models.CharField(max_length=100)
    detail_address = models.CharField(max_length=100, null=True, blank=True)
    requirement = models.TextField(blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=128, null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True, unique=True, region="KR")
    date_of_birth = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile/', default='default.png')
    addresses = models.ManyToManyField(Address)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

