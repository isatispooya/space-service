from rest_framework import serializers
from . import models  
from rest_framework import serializers


class CustomerRemainSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=models.Customer.objects.all())

    class Meta:
        model = models.CustomerRemain
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'



class BrokerageTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BrokerageTransactions
        fields = '__all__'

