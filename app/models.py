from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=200, null = True, unique=True)
    email = models.EmailField(unique=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [] 

    def __str__(self):
        return self.username