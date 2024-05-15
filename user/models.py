from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

class User(models.Model):
    '''
    first_name => نام برای حقیقی و نام کامل برای حقوقی
    last_name => نام خانوادگی برای حقیقی و برای حقوقی خالی
    national_code => شناسه ملی یا کد ملی
    is_person => فرد حقیقی است
    issue => محل صدور
    email => ایمیل
    password => رمزعبور
    status => وضعیت فعال/غیرفعال
    create_at => تاریخ ایجاد
    expiration => تاریخ اعتبار فعالیت
    mobile => شماره همراه
    phone => شماره ثابت
    address => آدرس پستی
    profile_picture => تصویر پروفایل
    date_birth => تاریخ تولد
    gender => جنسیت
    date_last_act => تاریخ اخرین فعالیت
    card_number_bank => شماره کارت بانکی
    marital => وضعیت تاهل
    
    '''
    first_name: models.CharField(max_length=255) #نام
    last_name: models.CharField(max_length=255, null=True, blank=True) #نام خانوادگی
    national_code = models.CharField(max_length=11, unique=True) #کد ملی یا شناسه ملی شرکت
    is_person = models.BooleanField(default=True) # حقیق است
    issue = models.CharField(max_length=75,null=True, blank=True) # محل صدور
    email = models.EmailField(unique=True,null=True,blank=True) #ایمیل
    password = models.CharField(max_length=32) #رمز عبور
    status = models.BooleanField(default=True) #فعال/غیرفعال وضعیت
    create_at = models.DateTimeField(auto_now_add=True) #تاریخ ایجاد
    expiration = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=180)) #تاریخ انقضای حساب 
    mobile = models.CharField(max_length=11,validators=[RegexValidator(r'^\d{11}$', message='شماره همراه صحیح نیست')],unique=True)
    phone = models.CharField(max_length=11,validators=[RegexValidator(r'^\d{11}$', message='شماره ثابت صحیح نیست')],null=True, blank=True)
    address = models.CharField(max_length=255,null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_images/',null=True, blank=True)
    date_birth = models.DateField(null=True, blank=True)
    GENDER_CHOICES = [('M', 'مرد'),('F', 'زن'),('U', 'نامشخص'),('C', 'حقوقی'),]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U')
    date_last_act = models.DateTimeField(default=timezone.now)
    card_number_bank = models.CharField(max_length=16,null=True, blank=True)
    shaba_bank = models.CharField(max_length=26,null=True, blank=True)
    marital = models.BooleanField(default=False)
    

