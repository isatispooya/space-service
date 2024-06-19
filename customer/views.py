from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status , generics
from . import models
import random
from users  import serializers
import datetime
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import get_resolver
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from . import serializers


# customer
class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    permission_classes = [IsAuthenticated]

# customer
class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    permission_classes = [IsAuthenticated]




# Custome Remain    
class CustomerRemainListCreateView(generics.ListCreateAPIView):
    queryset = models.CustomerRemain.objects.all()
    serializer_class = serializers.CustomerRemainSerializer
    permission_classes = [IsAuthenticated]

# Customer Remain    
class CustomerRemainDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CustomerRemain.objects.all()
    serializer_class = serializers.CustomerRemainSerializer
    permission_classes = [IsAuthenticated]


# Brokerage Transactions
class BrokerageTransactionsListCreateView(generics.ListCreateAPIView):
    queryset = models.BrokerageTransactions.objects.all()
    serializer_class = serializers.BrokerageTransactionsSerializer
    permission_classes = [IsAuthenticated]

# Brokerage Transactions
class BrokerageTransactionsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.BrokerageTransactions.objects.all()
    serializer_class = serializers.BrokerageTransactionsSerializer
    permission_classes = [IsAuthenticated]

