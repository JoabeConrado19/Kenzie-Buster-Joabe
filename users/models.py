from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    email = models.CharField(unique=True, null=False, max_length=127)
    first_name = models.CharField(null= False, max_length=50)
    last_name = models.CharField(null=False, max_length=50)
    birthdate = models.DateField(null=True)
    is_employee = models.BooleanField(null=True, default=False)
    is_superuser = models.BooleanField(null=True, default=False)
    
