
from rest_framework import serializers
from . import models  # جایگزین YourModel با مدل مورد نظر خود شوید
from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'national_code', 'is_person', 'issue', 'status', 'create_at', 'expiration', 'mobile', 'phone', 'address', 'profile_picture', 'date_birth', 'gender', 'date_last_act', 'card_number_bank', 'shaba_bank', 'marital']



class OtpModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Otp
        fields = '__all__'  # یا فیلدهای مورد نظرتان را به جای '__all__' قرار دهید
# class PositionGroupModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.PositionGroup
#         fields = '__all__'  # یا فیلدهای مورد نظرتان را به جای '__all__' قرار دهید
class CompanyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'  # یا فیلدهای مورد نظرتان را به جای '__all__' قرار دهید
# class PositionModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Position
#         fields = '__all__'  # یا فیلدهای مورد نظرتان را به جای '__all__' قرار دهید
# class EmployeePositionModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.EmployeePosition
#         fields = '__all__'  # یا فیلدهای مورد نظرتان را به جای '__all__' قرار دهید


class PositionGroupModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PositionGroup
        fields = '__all__'

class PositionModelSerializer(serializers.ModelSerializer):
    group = PositionGroupModelSerializer()
    
    class Meta:
        model = models.Position
        fields = '__all__'

class ClientUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClientUser
        fields = '__all__'

class EmployeePositionModelSerializer(serializers.ModelSerializer):
    user = models.ClientUser()
    position = PositionModelSerializer()
    
    class Meta:
        model = models.EmployeePosition
        fields = '__all__'

class CompanyWithEmployeesSerializer(serializers.ModelSerializer):
    employees = serializers.SerializerMethodField()

    class Meta:
        model = models.Company
        fields = '__all__'
    
    def get_employees(self, obj):
        employees = models.EmployeePosition.objects.filter(company=obj)
        return EmployeePositionModelSerializer(employees, many=True).data



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'


class ShareholderSerializer(serializers.ModelSerializer):   
    user_detail = serializers.SerializerMethodField()

    class Meta:
        model = models.Shareholder
        fields = '__all__'

    def get_user_detail(self, obj):
        user = obj.user
        return UserSerializer(user).data


    def get_company_detail(self, obj):
        company = obj.company
        return CompanyModelSerializer(company).data
    


    class ClientUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = models.ClientUser
            fields = '__all__'
            