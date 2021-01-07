from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    reg_no = models.TextField(unique=True)
    email = models.TextField()
    mobile_no = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)