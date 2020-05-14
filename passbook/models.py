from django.db import models
from users.models import CustomUser
from accounts.models import Account
from django.db.models.signals import post_save
from django.dispatch import receiver

class Passbook(models.Model):
    no=models.PositiveIntegerField(default=-1,null=True,blank=True)
    transaction_type=models.CharField(max_length=50,default="",null=False,blank=False)
    amount_transfered_to=models.PositiveIntegerField(default=0,null=True,blank=True)
    Initial_amount=models.PositiveIntegerField(default=0,null=True,blank=True)
    Final_amount=models.PositiveIntegerField(default=0,null=True,blank=True)

    def __str__(self):
        return str(self.no)
