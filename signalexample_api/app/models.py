from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=20)
    available_copies=models.IntegerField()

    def __str__(self):  #returns the string representation book object
        return self.title

class BookIssue(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    student_name=models.CharField(max_length=20)
    issued_date=models.DateTimeField(auto_now_add=True)
    due_date=models.DateTimeField(null=True,blank=True)

    def __str__(self):  #returns the string representation bookissue object
        return self.student_name