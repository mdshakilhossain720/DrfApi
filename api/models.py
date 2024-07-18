from django.db import models

# Create your models here.

class Carlist(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    des = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    color = models.CharField(max_length=100)
    prices=models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)