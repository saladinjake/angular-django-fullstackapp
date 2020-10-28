from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Book(models.Model):
    #owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=70, blank=False, default='')
    subtitle = models.CharField(max_length=200,blank=False, default='')
    author = models.CharField(max_length=50,blank=False, default='')
    isbn = models.CharField(max_length=80,blank=False, default='')

    def __str__(self):
        return self.title
