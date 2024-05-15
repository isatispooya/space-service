from rest_framework import serializers
from . import models  # جایگزین YourModel با مدل مورد نظر خود شوید

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'  # یا فیلدهای مورد نظرتان را به جای '__all__' قرار دهید
