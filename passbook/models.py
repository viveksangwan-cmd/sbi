from django.db import models
from users.models import CustomUser
from accounts.models import Account
from django.db.models.signals import post_save
from django.dispatch import receiver

class Passbook(models.Model):
    unique_no=models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True,default=-1)
    transaction_type=models.CharField(max_length=50,default="",null=False,blank=False)
    amount_transfered_to=models.PositiveIntegerField(default=0,null=True,blank=True)
    Initial_amount=models.PositiveIntegerField(default=0,null=True,blank=True)
    Final_amount=models.PositiveIntegerField(default=0,null=True,blank=True)


class connectnew():
    @receiver(post_save,sender=CustomUser)
    def create_new_passbook(sender,instance,created,**kwargs):
        if created:
            passbook=Passbook.objects.create(unique_no=instance)

    post_save.connect(create_new_passbook,sender=CustomUser)
