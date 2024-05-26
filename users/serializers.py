
from rest_framework import serializers
from . import models  # جایگزین YourModel با مدل مورد نظر خود شوید
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'national_code', 'is_person', 'issue', 'status', 'create_at', 'expiration', 'mobile', 'phone', 'address', 'profile_picture', 'date_birth', 'gender', 'date_last_act', 'card_number_bank', 'shaba_bank', 'marital']



class OtpModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Otp
        fields = '__all__'  # یا فیلدهای مورد نظرتان را به جای '__all__' قرار دهید
