from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from .models import Account
class Balance(TemplateView):
    template_name='accounts/balance.html'

def debit(request):
    amount=request.POST['amount']
    if amount!='':
        amount=int(request.POST['amount'])
        my_account=Account.objects.get(owner=request.user)
        print(my_account)
        print("before : ",my_account.balance)
        if amount>my_account.balance:
            print(my_account.balance-amount)
            print("No Sufficient balance")
        else:
            my_account.balance-=amount
        my_account.save()
        print("After ",my_account.balance)
    return redirect('account')

def credit(request):
    amount=request.POST['amount']
    if amount!='':
        amount=int(request.POST['amount'])
        my_account=Account.objects.get(owner=request.user)
        print(my_account)
        print("before : ",my_account.balance)
        my_account.balance+=amount
        my_account.save()
        print("After ",my_account.balance)
    return redirect('account')

def balance(request):
    my_account=Account.objects.get(owner=request.user)
    return render(request,'accounts/balance.html',{'balance':my_account.balance})
