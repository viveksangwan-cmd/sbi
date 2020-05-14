from django.shortcuts import render
from .models import Passbook
from django.db import connection
from users.models import CustomUser
class Update():
    def update_entry(No,type="",amount_to=0,initial=0,final=0):
        print(type,amount_to,initial,final)
        my_entry=Passbook(no=No,transaction_type=type,amount_transfered_to=0,Initial_amount=initial,Final_amount=final)
        my_entry.save()
        
