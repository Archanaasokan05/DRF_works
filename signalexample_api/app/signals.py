
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from app.models import BookIssue
from datetime import timedelta

## Use post_save signal to automatically reduce the value of available copies whenever
## a book is issued to student and also calculate due_date automatically

@receiver(post_save,sender=BookIssue)
def handle_bookissue_created(sender,instance,created,**kwargs):
    if created:
    # due_date
        instance.due_date=instance.issued_date+timedelta(days=14)
        instance.save(update_fields=['due_date'])   #update_fields -> only update the column ,otherwise recursion occurs
    # decrements available copies of book by 1
        book=instance.book
        book.available_copies-=1
        book.save(update_fields=['available_copies'])


## Use post_delete signals automatically increments available_copies by 1 whenever a book issue record deleted

@receiver(post_delete,sender=BookIssue)
def handle_bookissue_deleted(sender,instance,**kwargs):
    book = instance.book
    book.available_copies += 1
    book.save(update_fields=['available_copies'])


