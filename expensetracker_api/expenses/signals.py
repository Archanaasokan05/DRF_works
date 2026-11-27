from django.dispatch import receiver
from django.db.models.signals import post_save
from expenses.models import Expense

# @receiver(post_save,sender=Expense)
# def fun(sender,instance,created,**kwargs):  # Created flag only in post_save
#     print("hello")


# sender -Source model that sends notification/signal(post_save,pre_save,post_delete,pre_delete)

# receiver -fun that executes after receiving notification from sender

# instance --model object

# @receiver -decorator used to connect sender and receiver
from django.db.models.signals import post_delete

@receiver(post_delete,sender=Expense)
def fun(sender,instance,**kwargs):
    print("deleted")