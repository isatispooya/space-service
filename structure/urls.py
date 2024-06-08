from django.urls import path
from .views import MenuListView

urlpatterns = [
    path('menus/', MenuListView.as_view(), name='menu-list'),
]
