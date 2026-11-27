from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    category_choices=(('food','Food'),
                      ('bill','Bill'),
                      ('entertainment','Entertainment'),
                      ('shopping','Shopping'),
                      ('health','Health'),
                      ('others','Others'))

    priority_choices=(('need','Need'),('want','Want'))

    payment_choices=(('upi','Upi'),('cash','Cash'))

    title=models.CharField(max_length=30)
    amount=models.IntegerField()
    category=models.CharField(max_length=20,choices=category_choices)
    priority=models.CharField(max_length=20,choices=priority_choices)
    payment_method=models.CharField(max_length=20,choices=payment_choices)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)