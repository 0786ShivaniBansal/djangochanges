import imp
from attr import fields
from django.forms import models
from rest_framework import serializers
from accounts . models import Register

class register(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields='__all__'
       