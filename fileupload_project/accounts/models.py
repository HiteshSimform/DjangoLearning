from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('editor', 'Editor'),
        ('viewer', 'Viewer'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='viewer')
    address = models.CharField(max_length=100,blank=True,null=True)

    class Meta:
        db_table = 'auth_user'
        abstract = False

class abcd(CustomUser):
    pass

class x(abcd):
    xrole = models.CharField(max_length=10)
    class Meta:
        abstract = True

class y(models.Model):
    yrole = models.CharField(max_length=10)
    class Meta:
        abstract = True

class z(models.Model):
    zrole = models.CharField(max_length=10)
    class Meta:
        abstract = True

class t(y,z):
    pass

class pqrs(x,y):
    pass