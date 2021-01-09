from django.db import models
# Import for signal token generate
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    reg_no = models.TextField(unique=True)
    email = models.TextField()
    mobile_no = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Using signal to generate the token automatically when user is created code below
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
