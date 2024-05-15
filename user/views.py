from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from GuardPyCaptcha.Captch import GuardPyCaptcha
from .models import User
from .serializers import UserModelSerializer
class Captcha(APIView):
    def get(self, request):
        captchas = GuardPyCaptcha()
        captchas = captchas.Captcha_generation(num_char = 4, only_num = True)
        return Response(captchas,status=status.HTTP_200_OK)

class Otp(APIView):
    def post(self,request):
        captchas = GuardPyCaptcha()
        captchas = captchas.check_response(request.data['encrypted_response'],request.data['captcha'])
        if not True : #captchas
            result= {'message': 'کد کپچا صحیح نیست'}
            return Response(result,status=status.HTTP_406_NOT_ACCEPTABLE)
        print(request.data['mobile'])
        
        try:
            user = User.objects.get(mobile=request.data['mobile'])
        except:
            result= {'message': 'شماره همراه موجود نیست'}
            return Response(result,status=status.HTTP_404_NOT_FOUND)
        serialized_user = UserModelSerializer(user)
        

        print(serialized_user)

        result ={'message':'its ok'}
        return Response(result,status=status.HTTP_200_OK)
        
        
        
        
        