from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    '''
    Creating a new model to assign Category to category fields in the Content
    '''
    name = models.CharField(max_length=200,unique=True)
    def __str__(self):
        return self.name

class Content(models.Model):
    title = models.CharField(max_length=30, blank=False, unique=True)
    body = models.TextField(max_length=300, blank=True, unique=True)
    summary = models.CharField(max_length=30, blank=False, unique=True)
    document = models.FileField(upload_to='doc/', null=True, blank=True)
    category = models.ManyToManyField(Category)
    