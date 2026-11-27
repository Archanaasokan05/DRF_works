from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# Task model with five fields: `user` (foreign key), `title`, `description`, `created` timestamp, and `completed` (boolean).
class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    description=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    completed=models.BooleanField(default=False)
