from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from GuardPyCaptcha.Captch import GuardPyCaptcha
from .models import ClientUser,Otp
from . import models
import random
from .serializers import UserSerializer,OtpModelSerializer,CompanyWithEmployeesSerializer
from . import serializers
import datetime
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.permissions import IsAuthenticated

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
        if not captchas : 
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
    
    
class CompaniesViewset(APIView) :
    def post(self, request, format=None):
        serializer = serializers.CompanyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get (self , request) :
        companies = models.Company.objects.all()
        companies = serializers.CompanyModelSerializer(companies , many = True)
        print (companies.data)
        return Response (companies.data,status=status.HTTP_200_OK)





class CompanyWithEmployeesViewset(APIView):
    def post(self, request):
        companyid = request.data.get('company')

        CompanyWithEmployees = models.Company.objects.get(id = companyid)
        CompanyWithEmployees = CompanyWithEmployeesSerializer(CompanyWithEmployees)
        return Response(CompanyWithEmployees.data, status=status.HTTP_200_OK)
    





class CustomerViewset(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = serializers.CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        customers = models.Customer.objects.all()
        serializer = serializers.CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    





class ShareholderViewset(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = serializers.ShareholderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        company_id = request.data.get('company')
        if company_id:
            shareholders = models.Shareholder.objects.filter(company_id=company_id)
        else:
            shareholders = models.Shareholder.objects.all()
        
        serializer = serializers.ShareholderSerializer (shareholders, many=True)
        return Response(serializer.data)
    


class ClientUserViewset(APIView):
    queryset = ClientUser.objects.all()

    def post(self, request, format=None):
        serializer = serializers.ClientUserModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def get(self, request, format=None):
        username = request.data.get('username')
        # username = request.query_params.get('username')
        if username:
            client_user = models.ClientUser.objects.filter(username=username)
        else:
            client_user = models.ClientUser.objects.all()
        
        serializer = serializers.ClientUserModelSerializer(client_user, many=True)
        return Response(serializer.data)
    

class ClientUserWithNationalCodeViewset (APIView) :
    queryset = ClientUser.objects.all()

    def get (self , request , format=None) :
        national_code = request.data.get('national_code')
        if national_code :
            client_user = models.ClientUser.objects.filter (national_code=national_code)
        else :
            client_user = models.ClientUser.objects.all()
        serializer = serializers.ClientUserModelSerializer(client_user, many=True)
        return Response(serializer.data)
 


 