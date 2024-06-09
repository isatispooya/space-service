from django.urls import path
from .views import CaptchaViewset, OtpViewset,LoginViewset,CompaniesViewset,CompanyWithEmployeesViewset, CustomerViewset, ShareholderViewset,ClientUserViewset, ClientUserWithNationalCodeViewset,PermissionsViewset,GroupsViewset


urlpatterns = [
    path('captcha/', CaptchaViewset.as_view(), name='captcha'),
    path('otp/', OtpViewset.as_view(), name='otp'),
    path('login/', LoginViewset.as_view(), name='login'),
    path('companies/', CompaniesViewset.as_view(), name='companies'),
    path('companieswithemployees/', CompanyWithEmployeesViewset.as_view(), name='companieswithemployees'),
    path('customer/', CustomerViewset.as_view(), name='customer'),
    path('shareholder/', ShareholderViewset.as_view(), name='shareholder'),
    path('user/', ClientUserViewset.as_view(), name='user'),
    path('usernationalcode/',ClientUserWithNationalCodeViewset.as_view(), name='usernationalcode'),
    path('permissions/',PermissionsViewset.as_view(), name='permissions'),
    path('groups/',GroupsViewset.as_view(), name='groups'),
]







