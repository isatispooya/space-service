from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status , generics
from GuardPyCaptcha.Captch import GuardPyCaptcha
from .models import ClientUser,Otp
from . import models
import random
from .serializers import UserSerializer,OtpModelSerializer,CompanyWithEmployeesSerializer
from . import serializers
import datetime
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import get_resolver
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404




class CaptchaViewset(APIView):
    def get(self, request):
        captchas = GuardPyCaptcha()
        captchas = captchas.Captcha_generation(num_char = 4, only_num = True)
        return Response(captchas,status=status.HTTP_200_OK)
    

class OtpViewset(APIView):
    def post(self,request):
        captchas = GuardPyCaptcha()
        print(request.data)
        captchas = captchas.check_response(request.data['encrypted_response'],request.data['captcha'])
        if False: #not captchas : 
            result= {'message': 'کد کپچا صحیح نیست'}
            return Response(result,status=status.HTTP_406_NOT_ACCEPTABLE)
        mobile = request.data['mobile']
        try:
            user = ClientUser.objects.get(mobile=mobile)
        except:
            result= {'message': 'شماره همراه موجود نیست'}
            return Response(result,status=status.HTTP_404_NOT_FOUND)
        serialized_user = UserSerializer(user)

        code = 11111 #random.randint(10000,99999)
        otp = Otp(mobile=mobile,code =code)
        otp.save()

        result = {'success': True, 'message': 'کد تأیید ارسال شد'}
        return Response(result,status=status.HTTP_200_OK)

class LoginViewset (APIView) :
    def post (self,request) :
        mobile = request.data.get('mobile')
        code = request.data.get('code')
        
        if not mobile or not code:
            return Response({'message': 'شماره همراه و کد تأیید لازم است'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = ClientUser.objects.get(mobile=mobile)
        except:
            result = {'message': 'شماره موبایل موجود نیست'}
            return Response(result, status=status.HTTP_404_NOT_FOUND)
        
        try:
            otp_obj = Otp.objects.filter(mobile=mobile , code = code ).order_by('-date').first()
        except :
            
            return Response({'message': 'کد تأیید نامعتبر است'}, status=status.HTTP_400_BAD_REQUEST)
        
        otp = OtpModelSerializer(otp_obj).data
        if otp['code']== None :
            result = {'message': 'کد تأیید نامعتبر است'}
            return Response(result, status=status.HTTP_400_BAD_REQUEST)
        
        dt = datetime.datetime.now(datetime.timezone.utc)-datetime.datetime.fromisoformat(otp['date'].replace("Z", "+00:00"))
        
        dt = dt.total_seconds()

        if dt >120 :
            result = {'message': 'کد معتبر نیست'}
            return Response(result, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = ClientUser.objects.get(mobile=mobile)
        except ClientUser.DoesNotExist:
            return Response({'message': 'کاربری با این شماره همراه وجود ندارد'}, status=status.HTTP_404_NOT_FOUND)
        
        otp_obj.delete()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    
    

# companies
class CompaniesListCreateView(generics.ListCreateAPIView):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    permission_classes = [IsAuthenticated]

# companies
class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    permission_classes = [IsAuthenticated]

# employeeposition
class EmployeePositionListCreateView(generics.ListCreateAPIView):
    queryset = models.EmployeePosition.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.EmployeePositionModelSerializer

# employeeposition
class EmployeePositionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.EmployeePosition.objects.all()
    serializer_class = serializers.EmployeePositionModelSerializer
    permission_classes = [IsAuthenticated]


# shareholder
class ShareholderListCreateView(generics.ListCreateAPIView):
    queryset = models.Shareholder.objects.all()
    serializer_class = serializers.ShareholderSerializer
    permission_classes = [IsAuthenticated]

# shareholder
class ShareholderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Shareholder.objects.all()
    serializer_class = serializers.ShareholderSerializer
    permission_classes = [IsAuthenticated]

# position
class PositionListCreateView(generics.ListCreateAPIView):
    queryset = models.Position.objects.all()
    serializer_class = serializers.PositionModelSerializer
    permission_classes = [IsAuthenticated]

# positiongroup
class PositionGroupListCreateView(generics.ListCreateAPIView):
    queryset = models.PositionGroup.objects.all()
    serializer_class = serializers.PositionGroupModelSerializer
    permission_classes = [IsAuthenticated]

# clientuser
class ClientUserListCreateView(generics.ListCreateAPIView):
    queryset = models.ClientUser.objects.all()
    serializer_class = serializers.ClientUserModelSerializer
    permission_classes = [IsAuthenticated]

# clientuser
class ClientUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ClientUser.objects.all()
    serializer_class = serializers.ClientUserModelSerializer
    permission_classes = [IsAuthenticated]


# premission
class PermissionListCreateView(generics.ListCreateAPIView):
    queryset = models.Userpermissions.objects.all()
    serializer_class = serializers.PermissionsSerializer
    permission_classes = [IsAuthenticated]

# premission
class PermissionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Userpermissions.objects.all()
    serializer_class = serializers.PermissionsSerializer
    permission_classes = [IsAuthenticated]

# group
class GroupsListCreateView(generics.ListCreateAPIView):
    queryset = models.Groups.objects.all()
    serializer_class = serializers.GroupsSerializer
    permission_classes = [IsAuthenticated]

# group
class GroupsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Groups.objects.all()
    serializer_class = serializers.GroupsSerializer
    permission_classes = [IsAuthenticated]



# The priority of shareholders' transactions    اولویت معامله سهامدارن
class ShareholdersTransactionsListCreateView(generics.ListCreateAPIView):
    queryset = models.ShareholdersTransactions.objects.all()
    serializer_class = serializers.ShareholdersTransactionsSerializer
    permission_classes = [IsAuthenticated]

# The priority of shareholders' transactions    اولویت معامله سهامدارن
class ShareholdersTransactionsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ShareholdersTransactions.objects.all()
    serializer_class = serializers.ShareholdersTransactionsSerializer
    permission_classes = [IsAuthenticated]




