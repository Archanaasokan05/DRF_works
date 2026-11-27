from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    role_choices=(('organizer','Organizer'),
                  ('customer','Customer'))
    role=models.CharField(max_length=20,choices=role_choices)
    phone=models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        return self.username
