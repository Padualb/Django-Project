#from turtle import title

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)


class Place(models.Model):
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=200)
    slug = models.SlugField()
    district = models.CharField(max_length=20)
    free_entrance = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover = models.ImageField(upload_to='')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    category = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
