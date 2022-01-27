from pyexpat import model
from attr import fields
from django.forms import models
from rest_framework import serializers
from hello . models import User


class userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['idname'] 
    

