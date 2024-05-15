from django.urls import path
from .views import Captcha, Otp

urlpatterns = [
    path('captcha/', Captcha.as_view(), name='captcha'),
    path('otp/', Otp.as_view(), name='otp'),
]
