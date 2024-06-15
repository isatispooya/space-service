from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Customer, CustomerRemain
 

admin.site.register(Customer)
admin.site.register(CustomerRemain)