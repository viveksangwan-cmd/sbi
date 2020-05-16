from django.shortcuts import render
from .models import Passbook
from django.db import connection
from users.models import CustomUser
class Update():
    def update_entry(No,type="",amount_to=0,initial=0,final=0):
        print("Passbook : ",type,amount_to,initial,final)
        my_entry=Passbook(no=No,transaction_type=type,amount_transfered_to=amount_to,Initial_amount=initial,Final_amount=final)
        my_entry.save()
class Statement():
    def return_passbook_statement(user_account):
        print("In Passbook Section From Passbook")
        data=Passbook.objects.filter(no=user_account)
        print(data)
        return data

    def return_mini_statement(user_account):
        print("In Passbook Section From MiniStatement")
        data=reversed(Passbook.objects.filter(no=user_account).order_by('no')[::-1][:10])
        print(data)
        return data
