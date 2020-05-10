from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect

class Balance(TemplateView):
    template_name='balance.html'

def debit(request):
    amount=int(request.POST['amount'])
    my_account=Account.objects.filter(user=request.user)
    my_account.balance-=amount
    my_account.save()
    return redirect("/")

def credit(request):
    amount=int(request.POST['amount'])
    my_account=Account.objects.filter(user=request.user)
    my_account.balance+=amount
    my_account.save()
    return redirect("/")
