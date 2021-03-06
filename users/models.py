from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    Image=models.ImageField(default="default.jpg",null=True,blank=True)
    Firstname=models.CharField(max_length=50,default="",null=False,blank=False)
    Lastname=models.CharField(max_length=50,default="",null=False,blank=False)
    age=models.PositiveIntegerField(null=True,blank=True)
    Email_ID= models.EmailField(max_length = 254,null=False,blank=False)
    unique_no=models.AutoField(primary_key=True)
