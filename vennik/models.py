from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    description = models.CharField(max_length=120 ,default='' )
    email = models.CharField(max_length=120 ,default='')
    phone =models.IntegerField(default=0)
    department = models.CharField(max_length=100,default='',)


def create_Profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_Profile,sender=User)

class Apartment(models.Model):
    location=models.CharField(max_length=50, default='')
    price=models.IntegerField(default=0)
    type=models.CharField(default="", max_length=50)
    description = models.CharField(default='', max_length=50)
    # apartmentName=models.OneToOneField(Group, on_delete=models.CASCADE)
class Good(models.Model):
    price = models.IntegerField(default=0)
    description = models.CharField(default='', max_length=50) 
    # name=models.OneToOneField(Group, on_delete=models.CASCADE)

# def createItem(sender,**kwargs):
    # if (kwargs['created'] == Apartment):
    #     itemCreated=Apartment.objects.create(apartmentName=kwargs['instance'])
    # elif (kwargs['created']== Good):
    #     itemCreated=Good.objects.create(name=kwargs['instance'])

# post_save.connect(createItem,sender=Group)