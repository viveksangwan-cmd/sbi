import random
from .utils import create_new_account_number
from django.db import models
from users.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class Account(models.Model):
    unique_no=models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)
    account_number = models.CharField(max_length = 10,blank=True,editable=False,unique=True,default=create_new_account_number())
    balance=models.PositiveIntegerField(default=0,null=False,blank=True)

    def __str__(self):
        return str(self.unique_no)+" "+str(self.account_number)

class connectnew():
    @receiver(post_save,sender=CustomUser)
    def create_new_account(sender,instance,created,**kwargs):
        if created:
            account=Account.objects.create(unique_no=instance)

    post_save.connect(create_new_account,sender=CustomUser)
