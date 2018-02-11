from django.db import models
import datetime
from django.utils import timezone
from datetime import datetime

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name+" "+self.last_name

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    