from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from .models import Account
from passbook.views import return_mini_statement,return_passbook_statement,update_entry
from users.models import CustomUser
from django.contrib.auth.decorators import login_required
@login_required(login_url='home')
def passbook(request):
    my_account=Account.objects.get(unique_no=request.user)
    data=return_passbook_statement(user_account=my_account.account_number)
    print(data)
    return render(request,'accounts/passbook.html',{'data':data})

@login_required(login_url='home')
def miniStatement(request):
    my_account=Account.objects.get(unique_no=request.user)
    data=return_mini_statement(user_account=my_account.account_number)
    print(data)
    return render(request,'accounts/miniStatement.html',{'data':data})

@login_required(login_url='home')
def balance(request):
    my_account=Account.objects.get(unique_no=request.user)
    return render(request,'accounts/balance.html',{'balance':my_account.balance})

@login_required(login_url='home')
def transfer(request):
    amount=request.POST['amount']
    account_no=request.POST['account_no']
    if amount!='' and account_no!='':
        amount=int(request.POST['amount'])
        account_holder_name=request.POST['username']
        my_account=Account.objects.get(unique_no=request.user)
        print(amount,account_no)
        print("Transfer From :",my_account.account_number)
        initial=my_account.balance
        print("Transfer_From initial : ",initial)
        try:
            transfer_account_no=Account.objects.get(account_number=account_no)
            Transfer_usrername=CustomUser.objects.get(account=transfer_account_no)
            if account_holder_name!=Transfer_usrername.username:
                raise Exception
            if amount>initial:
                print("Insufficient Fund")
                raise Exception
            print("Correct account holder name and account number.")
            message="Provided account number is not linked with bank."
            print("Transfer_To : ",transfer_account_no)
            transfer_initial=transfer_account_no.balance
            print("Transfer_To initial : ",transfer_initial)
            transfer_account_no.balance+=amount
            print("Transfer_To Final ",transfer_account_no.balance)
            my_account.balance-=amount
            transfer_account_no.save()
            my_account.save()
            update_entry(No=transfer_account_no.account_number,type="Transfer_From",amount_to=int(my_account.account_number),initial=transfer_initial,final=transfer_account_no.balance)
            update_entry(No=my_account.account_number,type="Transfer_To",amount_to=int(transfer_account_no.account_number),initial=initial,final=my_account.balance)
            print("After ",my_account.balance)
            return render(request,'accounts/transfer_success.html')
        except Exception as e:
            print(e)
            return render(request,'accounts/transfer_fail.html',{'Exception':e})
    else:
        print("Illegal no")
    return redirect('account')



@login_required(login_url='home')
def debit(request):
    amount=request.POST['amount']
    if amount!='':
        amount=int(request.POST['amount'])
        my_account=Account.objects.get(unique_no=request.user)
        print(my_account)
        initial=my_account.balance
        print("before : ",initial)
        if amount>my_account.balance:
            print(my_account.balance-amount)
            print("No Sufficient balance")
        else:
            my_account.balance-=amount
            update_entry(No=my_account.account_number,type="Debit",amount_to=my_account.account_number,initial=initial,final=my_account.balance)
        my_account.save()
        print("After ",my_account.balance)
    return redirect('account')

@login_required(login_url='home')
def credit(request):
    amount=request.POST['amount']
    if amount!='':
        amount=int(request.POST['amount'])
        my_account=Account.objects.get(unique_no=request.user)
        print(my_account)
        print("hiii :",my_account.account_number)
        initial=my_account.balance
        print("before : ",initial)
        my_account.balance+=amount
        update_entry(No=my_account.account_number,type="Credit",amount_to=int(my_account.account_number),initial=initial,final=my_account.balance)
        my_account.save()
        print("After ",my_account.balance)
    else:
        print('Illegal amount')
    return redirect('account')
