from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Post(models.Model):
    #owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
