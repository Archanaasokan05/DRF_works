from django.db import models
from recipies.models import Recipie
from django.contrib.auth.models import User
# Create your models here.

class Review(models.Model):
    recipe = models.ForeignKey(Recipie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    comment=models.TextField()
    rating=models.FloatField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username