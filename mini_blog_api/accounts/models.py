from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    phone=models.CharField(max_length=15,null=True,unique=True)
    bio=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.email