from django.db import models

# Create your models here.
class Register(models.Model):
    firstname=models.CharField(max_length=100,null=True,blank=True)
    rid=models.TextField(primary_key=True)
    contact=models.CharField(max_length=12,null=True,blank=True)
    emailid=models.EmailField(null=True,blank=True)
    img=models.ImageField(upload_to='img',null=True,blank=True)
    passcode=models.TextField(null=True,blank=True)


class Login(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    password=models.TextField(null=True,blank=True)