from django.db import models

# Create your models here.

class Point(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6,default=0)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    