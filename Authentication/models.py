from django.db import models
from django.utils.timezone import now





class Auth(models.Model):
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=64, unique=True)
    CreateAt = models.DateTimeField (default=now)
    class Meta:
        verbose_name = "Domain"
        verbose_name_plural = "Domains "
    def __str__(self):
        return self.name+ '(' + self.domain+')'