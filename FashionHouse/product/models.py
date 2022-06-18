from operator import truediv
from tkinter import image_names
from turtle import title
from unicodedata import category
from django.db import models

# Create your models here.


class Product(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.TextField(max_length=50, null=False, default='NA')
    description = models.TextField(null=False, default='NA')
    price = models.FloatField(null=False, default=0.0)
    color = models.TextField(null=False, default='Na')
    stock = models.BooleanField(null=False, default='NA')
    image = models.FileField(upload_to='upload', default='NA')
    size = models.FloatField(null=False, default='NA')
    category = models.TextField(null=False, default='Cloth')
    delivery = models.SmallIntegerField(null=False, default=5)  
