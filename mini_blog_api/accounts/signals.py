from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import CustomUser

@receiver(post_save,sender=CustomUser)
def message(sender,instance,created,**kwargs):
    if created:
        print("Welcome to our Blog!..")