from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Otp, Company, PositionGroup, Position, EmployeePosition,Customer , Shareholder

User = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password')

class CustomUserAdmin(DefaultUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'national_code', 'is_person', 'issue', 'mobile', 'phone', 'address', 'profile_picture', 'date_birth', 'gender', 'date_last_act', 'card_number_bank', 'shaba_bank', 'marital')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined', 'create_at', 'expiration')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'national_code', 'is_person', 'issue', 'mobile'),
        }),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Otp)
admin.site.register(Company)
admin.site.register(PositionGroup)
admin.site.register(Position)
admin.site.register(EmployeePosition)
admin.site.register(Customer)
admin.site.register(Shareholder)