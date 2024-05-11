from django.urls import path,include
from . import views
from rest_framework import routers




router = routers.DefaultRouter()
router.register(viewset=views.AuthViewSet, prefix='auth', basename='auth')

urlpatterns = [
    path('', include(router.urls)),
]
