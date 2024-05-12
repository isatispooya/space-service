from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

class User(models.Model):
    first_name: models.CharField(max_length=255) #نام
    last_name: models.CharField(max_length=255, null=True, blank=True) #نام خانوادگی
    national_code = models.CharField(max_length=11, unique=True) #کد ملی یا شناسه ملی شرکت
    is_person = models.BooleanField(default=True) # حقیق است
    issue = models.CharField(max_length=75,null=True, blank=True) # محل صدور
    email = models.EmailField(unique=True,null=True,blank=True)
    password = models.CharField(max_length=32)
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=180))
    mobile = models.CharField(validators=[RegexValidator(r'^\d{11}$', message='شماره همراه صحیح نیست')],unique=True)
    phone = models.CharField(validators=[RegexValidator(r'^\d{11}$', message='شماره ثابت صحیح نیست')],null=True, blank=True)
    address = models.CharField(max_length=255,null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_images/',null=True, blank=True)
    date_birth = models.DateField(null=True, blank=True)
    GENDER_CHOICES = [('M', 'مرد'),('F', 'زن'),('U', 'نامشخص'),('C', 'حقوقی'),]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U')
    date_last_act = models.DateTimeField(default=timezone.now())
    
    

