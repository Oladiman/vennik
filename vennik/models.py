from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    description = models.CharField(max_length=120 ,default='' )
    email = models.CharField(max_length=120 ,default='')
    phone =models.IntegerField(default=0)
    department = models.CharField(max_length=100,default='',)

class Location(models.Model):
    LocationName=models.CharField(max_length=50, default='')
    # pricerange=models.IntegerField(default='0')