from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from GuardPyCaptcha.Captch import GuardPyCaptcha
from .models import User,Otp
import random
from .serializers import UserModelSerializer,OtpModelSerializer
import datetime

class CaptchaViewset(APIView):
    def get(self, request):
        captchas = GuardPyCaptcha()
        captchas = captchas.Captcha_generation(num_char = 4, only_num = True)
        return Response(captchas,status=status.HTTP_200_OK)

class OtpViewset(APIView):
    def post(self,request):
        captchas = GuardPyCaptcha()
        captchas = captchas.check_response(request.data['encrypted_response'],request.data['captcha'])
        if not True : #captchas
            result= {'message': 'کد کپچا صحیح نیست'}
            return Response(result,status=status.HTTP_406_NOT_ACCEPTABLE)
        print(request.data['mobile'])
        mobile = request.data['mobile']
        
        try:
            user = User.objects.get(mobile=mobile)
        except:
            result= {'message': 'شماره همراه موجود نیست'}
            return Response(result,status=status.HTTP_404_NOT_FOUND)
        serialized_user = UserModelSerializer(user)

        code =random.randint(10000,99999)
        otp = Otp(mobile=mobile,code =code)
        otp.save()

        result ={'sucsses':True}
        return Response(result,status=status.HTTP_200_OK)
        
        
class LoginViewset (APIView) :
    def post (self,request) :
        mobile = request.data.get('mobile')
        code = request.data.get('code')
        
        try:
            user = User.objects.get(mobile=mobile)
        except:
            result = {'message': 'شماره موبایل موجود نیست'}
            return Response(result, status=status.HTTP_404_NOT_FOUND)
        
        try:
            otp = Otp.objects.filter(mobile=mobile , code = code ).order_by('-date').first()
            # otp = otp.first()
        except :
            result = {'message': 'کد صحیح نیست'}
            return Response(result, status=status.HTTP_400_BAD_REQUEST)
        otp = OtpModelSerializer(otp).data
        if otp['code']== None :
            result = {'message': 'کد صحیح نیست'}
            return Response(result, status=status.HTTP_400_BAD_REQUEST)
        dt = datetime.datetime.now(datetime.timezone.utc)-datetime.datetime.fromisoformat(otp['date'].replace("Z", "+00:00"))
        dt = dt.total_seconds()
        if dt >120 :
            result = {'message': 'کد معتبر نیست'}
            return Response(result, status=status.HTTP_400_BAD_REQUEST)
        uid = UserModelSerializer(user).data['national_code']
        

        result = { 'uid': uid}
        return Response(result, status=status.HTTP_200_OK)