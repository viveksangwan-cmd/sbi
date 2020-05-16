from django.views.generic.base import TemplateView
from django.urls import path
from .views import balance,debit,credit,transfer,passbook,miniStatement
from .views import *
urlpatterns=[
    path('',TemplateView.as_view(template_name='accounts/account.html'),name='account'),
    path('balance/',balance,name='balance'),
    path('creditBalance/',TemplateView.as_view(template_name='accounts/credit.html'),name='credit'),
    path('creditBalance/creditnow',credit,name='creditnow'),
    path('debitBalance/',TemplateView.as_view(template_name='accounts/debit.html'),name='debit'),
    path('debitBalance/debitnow',debit,name='debitnow'),
    path('transaction/',TemplateView.as_view(template_name='accounts/transaction.html'),name='transfer'),
    path('transaction/trsanction_now',transfer,name='trsanction_now'),
    path('passbook/',passbook,name='passbook'),
    path('MiniStatement/',miniStatement,name='miniStatement'),

]
