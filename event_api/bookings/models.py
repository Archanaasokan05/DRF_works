from django.db import models
from accounts.models import CustomUser
from events.models import Event
# Create your models here.


class Booking(models.Model):
    status_choices=(('pending','Pending'),
                    ('expired','Expired'),
                    ('confirmed','Confirmed'),
                    ('cancelled','Cancelled'))
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    seats=models.IntegerField()
    amount=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=30,choices=status_choices,default="pending")
    ticket_code=models.CharField(max_length=20,null=True,blank=True)