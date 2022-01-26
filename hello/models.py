from django.db import models


# Create your models here.
class User(models.Model):
    idname=models.IntegerField(primary_key=True)
    firstname=models.CharField(max_length=100,null=True,blank=True)
    lastname=models.CharField(max_length=100,null=True,blank=True)
    companyname=models.CharField(max_length=100,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    city=models.TextField(null=True,blank=True)
    state=models.TextField(null=True,blank=True)
    zip=models.TextField(null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    web=models.TextField(null=True,blank=True)
    
