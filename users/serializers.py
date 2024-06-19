
from rest_framework import serializers
from . import models  
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
        fields = '__all__'  

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'   


class PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Userpermissions
        fields = '__all__'



class GroupsSerializer(serializers.ModelSerializer):
    endpoint = serializers.PrimaryKeyRelatedField(queryset=models.Userpermissions.objects.all(), many=True)

    class Meta:
        model = models.Groups
        fields = '__all__'


class PositionGroupModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PositionGroup
        fields = '__all__'

class PositionModelSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(queryset=models.PositionGroup.objects.all())

    
    class Meta:
        model = models.Position
        fields = '__all__'



class ClientUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClientUser
        fields = '__all__'

class EmployeePositionModelSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=models.ClientUser.objects.all())
    position = serializers.PrimaryKeyRelatedField(queryset=models.Position.objects.all())
    company = serializers.PrimaryKeyRelatedField(queryset=models.Company.objects.all())
    class Meta:
        model = models.EmployeePosition
        fields = '__all__'


    

class ShareholdersTransactionsSerializer(serializers.ModelSerializer):
    seller = serializers.PrimaryKeyRelatedField(queryset=models.Shareholder.objects.all())
    buyer = serializers.PrimaryKeyRelatedField(queryset=models.Shareholder.objects.all())
    symbol = serializers.PrimaryKeyRelatedField(queryset=models.Company.objects.all())
    class Meta:
        model = models.ShareholdersTransactions
        fields = '__all__'


    

class CompanyWithEmployeesSerializer(serializers.ModelSerializer):
    employees = serializers.SerializerMethodField()

    class Meta:
        model = models.Company
        fields = '__all__'
    
    def get_employees(self, obj):
        employees = models.EmployeePosition.objects.filter(company=obj)
        return EmployeePositionModelSerializer(employees, many=True).data


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
        return CompanySerializer(company).data
    


    class ClientUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = models.ClientUser
            fields = '__all__'
    def get_user_detail(self, obj):
        user = obj.user
        return UserSerializer(user).data
    
