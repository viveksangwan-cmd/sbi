from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from .models import Account
from django.contrib.auth.mixins import LoginRequiredMixin
class Balance(LoginRequiredMixin,TemplateView):
    template_name='accounts/balance.html'

class Debit(LoginRequiredMixin):
    def debit(request):
        amount=request.POST['amount']
        if amount!='':
            amount=int(request.POST['amount'])
            my_account=Account.objects.get(unique_no=request.user)
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

class Credit(LoginRequiredMixin):
    def credit(request):
        amount=request.POST['amount']
        if amount!='':
            amount=int(request.POST['amount'])
            my_account=Account.objects.get(unique_no=request.user)
            print(my_account)
            print("before : ",my_account.balance)
            my_account.balance+=amount
            my_account.save()
            print("After ",my_account.balance)
        return redirect('account')
class Balance(LoginRequiredMixin):
    def balance(request):
        my_account=Account.objects.get(unique_no=request.user)
        return render(request,'accounts/balance.html',{'balance':my_account.balance})
