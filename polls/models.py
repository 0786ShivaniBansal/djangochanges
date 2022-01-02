from typing import Optional
from django.db import models

# Create your models here.
class Restaurent(models.Model):
    
    name = models.CharField(max_length=100,null=True,blank=True)
    descr = models.TextField(max_length=500,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    img = models.ImageField(upload_to='img',null=True,blank=True)
    offer = models.BooleanField(default=False,null=True,blank=True)