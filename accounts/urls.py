from django.views.generic.base import TemplateView
from django.urls import path
from .views import Balance,Debit,Credit
from .views import *
urlpatterns=[
    path('',TemplateView.as_view(template_name='accounts/account.html'),name='account'),
    path('balance/',Balance.balance,name='balance'),
    path('creditBalance/',TemplateView.as_view(template_name='accounts/credit.html'),name='credit'),
    path('creditBalance/creditnow',Credit.credit,name='creditnow'),
    path('debitBalance/',TemplateView.as_view(template_name='accounts/debit.html'),name='debit'),
    path('debitBalance/debitnow',Debit.debit,name='debitnow'),
]
