import random
from .utils import create_new_account_number
from django.db import models
from users.models import CustomUser

class Account(models.Model):
    owner=models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)
    account_number = models.CharField(max_length = 10,blank=True,editable=False,unique=True,default=create_new_account_number())
    balance=models.PositiveIntegerField(default=0,null=False,blank=True)

    def __str__(self):
        return str(self.owner)+" "+str(self.account_number)
