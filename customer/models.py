from django.db import models
from django.db import models
from django.utils import timezone

from users.models import ClientUser , Company 




# Customer   مشتریان
class Customer (models.Model) :
    user = models.ForeignKey(ClientUser, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return f'{self.user} {self.company}'

    class Meta:
        unique_together = ('user', 'company')



# Customer Remain
class CustomerRemain (models.Model) :

    '''
    adjusted_remain => مانده تعدیلی
    blocked_remain => مانده مسدود شده
    credit => اعتبار
    current_remain => مانده فعلی 
    customer => مشتری

    '''
    adjusted_remain = models.IntegerField () 
    blocked_remain =  models.IntegerField()
    credit = models.IntegerField()
    current_remain = models.IntegerField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE ,  unique=True)
    datetime = models.DateTimeField(default=timezone.now)

    def __str__ (self) :
        return f'{self.customer} {self.current_remain}'

  

# Brokerage Transactions     معاملات کارگزاری
class BrokerageTransactions (models.Model) :
    '''
    Index 
    AddedValueTax
    BondDividend
    BranchID => کد شعبه
    BranchTitle
    Discount
    InstrumentCategory
    MarketInstrumentISIN
    NetPrice
    Price
    TotalCommission
    TradeCode => کد معاملاتی
    TradeDate
    TradeItemBroker
    TradeItemRayanBourse
    TradeNumber
    TradeStationType
    TradeSymbol
    TradeType
    TransferTax
    Volume => حجم
    DateInt
    Update => به روزرسانی
    Name => نام
    Fund => صندوق
    Customer => مشتری
    '''
    Index = models.CharField (max_length= 150)
    AddedValueTax = models.IntegerField()
    BondDividend = models.IntegerField()
    BranchID = models.IntegerField()
    BranchTitle = models.CharField (max_length= 150)
    Discount = models.IntegerField()
    InstrumentCategory = models.BooleanField()
    MarketInstrumentISIN = models.CharField(max_length=150)
    NetPrice = models.IntegerField()
    Price = models.IntegerField ()
    TotalCommission = models.IntegerField ()
    TradeCode = models.IntegerField ()
    TradeDate = models.DateTimeField()
    TradeItemBroker = models.IntegerField ()
    TradeItemRayanBourse = models.IntegerField ()
    TradeNumber = models.IntegerField ()
    TradeStationType = models.BooleanField()
    TradeSymbol = models.CharField(max_length=200)
    TradeType = models.CharField(max_length=150)
    TransferTax = models.IntegerField ()
    Volume = models.IntegerField ()
    DateInt = models.IntegerField ()
    Update = models.DateTimeField(default=timezone.now())
    Name = models.CharField (max_length=200)
    Fund = models.BooleanField()
    Customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

    def __str__ (self) :
        return f'{self.Customer}'

