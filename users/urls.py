from django.urls import path
from .views import CaptchaViewset, OtpViewset,LoginViewset,ShareholdersTransactionsListCreateView,ShareholdersTransactionsDetailView,PositionGroupListCreateView,PositionListCreateView,EmployeePositionListCreateView,EmployeePositionDetailView, CustomerListCreateView,CustomerDetailView, ShareholderListCreateView,ShareholderDetailView,ClientUserListCreateView,ClientUserDetailView,PermissionListCreateView,PermissionDetailView,GroupsDetailView,GroupsListCreateView,CompaniesListCreateView,CompanyDetailView
# CompaniesViewset

urlpatterns = [
    path('captcha/', CaptchaViewset.as_view(), name='captcha'),
    path('otp/', OtpViewset.as_view(), name='otp'),
    path('login/', LoginViewset.as_view(), name='login'),
    path('position/',PositionListCreateView.as_view(), name='position'),
    path('positiongroup/',PositionGroupListCreateView.as_view(), name='positiongroup'),
    path('company/',CompaniesListCreateView.as_view(), name='company'),
    path('company/<int:pk>/',CompanyDetailView.as_view(), name='company'),
    path('employeeposition/',EmployeePositionListCreateView.as_view(), name='employeeposition'),
    path('employeeposition/<int:pk>/',EmployeePositionDetailView.as_view(), name='employeeposition'),
    path('customer/', CustomerListCreateView.as_view(), name='customer'),
    path('customer/<int:pk>/',CustomerDetailView.as_view(), name='customer'),
    path('user/', ClientUserListCreateView.as_view(), name='user'),
    path('user/<int:pk>/',ClientUserDetailView.as_view(), name='user'),
    path('shareholder/', ShareholderListCreateView.as_view(), name='shareholder'),
    path('shareholder/<int:pk>/',ShareholderDetailView.as_view(), name='shareholder'),
    path('permission/', PermissionListCreateView.as_view(), name='permission'),
    path('permission/<int:pk>/',PermissionDetailView.as_view(), name='permission'),
    path('groups/',GroupsListCreateView.as_view(), name='groups'),
    path('groups/<int:pk>/',GroupsDetailView.as_view(), name='groups'),
    path('shareholderstransactions/',ShareholdersTransactionsListCreateView.as_view(), name='shareholderstransactions'),
    path('shareholderstransactions/<int:pk>/',ShareholdersTransactionsDetailView.as_view(), name='shareholderstransactions'),

]







