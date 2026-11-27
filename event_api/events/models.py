from django.db import models
from accounts.models import CustomUser

# Create your models here.
# title,description,date,time,venue,created,organizer,amount,total_seats,available_seats,image

class Event(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField()
    date=models.DateField()
    time=models.TimeField()
    venue=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    organizer=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    amount=models.IntegerField()
    total_seats=models.IntegerField()
    available_seats=models.IntegerField()
    image=models.ImageField(null=True,upload_to='events')


    def __str__(self):
        return self.title
