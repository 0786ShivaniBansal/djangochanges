from distutils.command.upload import upload
from pickle import TRUE
from django.db import models

# Create your models here.
class reg(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    DOB=models.TextField(null=True,blank=True)
    phoneNumber=models.TextField(null=True,blank=True)
    img=models.ImageField(upload_to='img',null=True,blank=True)


class login(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    password=models.TextField(null=True,blank=True)