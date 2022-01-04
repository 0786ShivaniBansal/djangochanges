from os import name
from typing import Optional
from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.
class Restaurent(models.Model):
    
    name = models.CharField(max_length=100,null=True,blank=True)
    descr = models.TextField(max_length=500,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    img = models.ImageField(upload_to='img',null=True,blank=True)
    offer = models.BooleanField(default=False,null=True,blank=True)


class Fruits(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    color=models.CharField(max_length=100,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    
class User(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    id=models.BigAutoField(primary_key=True)
    Mobile=models.IntegerField(null=True,blank=True)
    Email=models.EmailField(null=True,blank=True)
    Password=models.TextField(null=True,blank=True)
    Admin=models.CharField(max_length=100,null=True,blank=True)
    Chef=models.CharField(max_length=100,null=True,blank=True)
    Waiter=models.CharField(max_length=100,null=True,blank=True)
