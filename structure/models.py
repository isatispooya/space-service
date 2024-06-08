from django.db import models

from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=200, unique=True)
    url = models.CharField(max_length=200, unique=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'
        ordering = ['title']
