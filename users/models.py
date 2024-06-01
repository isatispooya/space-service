from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, Group, Permission

class ClientUser(AbstractUser):
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
    username= models.CharField(max_length=100,  unique=True , null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    national_code = models.CharField(max_length=11, unique=True)
    is_person = models.BooleanField(default=True)
    issue = models.CharField(max_length=75, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    password = models.CharField(max_length=800)
    father = models.CharField(max_length=150 ,null=True, blank=True)
    bours_code = models.CharField(max_length=20 ,null=True, blank=True)
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(default=timezone.now)
    expiration = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=180))
    mobile = models.CharField(max_length=11, validators=[RegexValidator(r'^\d{11}$', message='شماره همراه صحیح نیست')], unique=True)
    phone = models.CharField(max_length=11, validators=[RegexValidator(r'^\d{11}$', message='شماره ثابت صحیح نیست')], null=True, blank=True)
    internal_number = models.CharField(max_length=11,null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    date_birth = models.DateField(null=True, blank=True)
    GENDER_CHOICES = [('M', 'مرد'), ('F', 'زن'), ('U', 'نامشخص'), ('C', 'حقوقی')]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U')
    date_last_act = models.DateTimeField(default=timezone.now)
    card_number_bank = models.CharField(max_length=16, null=True, blank=True)
    shaba_bank = models.CharField(max_length=26, null=True, blank=True)
    marital = models.BooleanField(default=False , null=True, blank=True)
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )


class Otp (models.Model) :
    '''
    mobile => شماره همراه
    code => کد 
    date => زمان
    '''
    mobile = models.CharField(max_length=11)
    code = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

class Company (models.Model) :
    '''
    name => نام شرکت
    national_id => شناسه ملی  
    address => آدرس 
    telephone => تلفن
    registration_number => شماره ثبت
    website => وبسایت
    Logo => لوگو 
    symbol => نماد
    register_capital => سرمایه ثبتی

    '''

    name = models.CharField(max_length=250)
    national_id = models.BigIntegerField()
    address  = models.CharField(max_length=1000)
    telephone = models.CharField(max_length=20)
    registration_number = models.IntegerField()
    website = models.CharField(max_length=800)
    Logo = models.ImageField (upload_to='IsatisSpace/static/images/' , blank=True, null=True)
    symbol = models.CharField(max_length=250)
    register_capital = models.BigIntegerField()
    def __str__(self):
        return f'{self.name}'
    
    
    
class PositionGroup(models.Model):
    '''
    name => نام گروه شغلی
    level => سطح یا ارشدیت گروه شغلی
    '''
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    def __str__(self):
        return f'{self.name} {self.level}'
    
    
class Position(models.Model):
    '''
    name => شغل / سمت
    group => گروه شغلی
    '''
    name = models.CharField(max_length=64)
    group = models.ForeignKey(PositionGroup, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name} {self.group}'

class EmployeePosition(models.Model):
    '''
    تعریف پرسنل بر اساس شرکت و شغل و شخص 
    user => ClientUserاطلاعات مرتبط با 
    company => Companyاطلاعات مرتبط با 
    position => Positionاطلاعات مرتبط با 
    '''
    user = models.ForeignKey(ClientUser, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} {self.position} {self.company}'
    

class Shareholder (models.Model):
    user = models.ForeignKey(ClientUser, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f'{self.user} {self.company}'



class Customer (models.Model) :
    user = models.ForeignKey(ClientUser, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return f'{self.user} {self.company}'

    class Meta:
        # تعیین کلید یکتا برای ترکیب user و company
        unique_together = ('user', 'company')
