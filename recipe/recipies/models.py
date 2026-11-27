from django.db import models

# Create your models here.
class Recipie(models.Model):    # table definition
    recipie_name=models.CharField(max_length=100)
    ingredients=models.TextField()
    instructions=models.TextField()
    mealtype=models.CharField(max_length=50)
    cusine=models.CharField(max_length=100)
    image=models.ImageField(upload_to='recipies/')

    def __str__(self):  # string representation of object
        # return self.cusine
        return self.recipie_name
        # return self.user.username