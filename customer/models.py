from django.db import models
from django.db import models
from django.utils import timezone

from users.models import ClientUser , Company 




# Customer مشتریان
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
    adjusted_remain = models.IntegerField () 
    blocked_remain =  models.IntegerField()
    credit = models.IntegerField()
    current_remain = models.IntegerField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now)

    def __str__ (self) :
        return f'{self.customer} {self.current_remain}'

  
