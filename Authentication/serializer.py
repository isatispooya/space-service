from rest_framework import serializers
from . import models
from rest_framework import generics


class Auth(serializers.ModelSerializer) :
    class Meta:
        model = models.Auth
        fields = '__all__' 
