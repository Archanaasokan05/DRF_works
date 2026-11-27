from django.db import models
from accounts.models import CustomUser


# Create your models here.

class Post(models.Model):
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    # author_email=models.CharField(max_length=50)
    title=models.CharField(max_length=30)
    content=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title