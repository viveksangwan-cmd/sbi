from django.urls import path
from .views import Balance,debit,credit
urlpatterns=[
    path('balance/',Balance.as_view(),name='balance'),
    path('debit/',debit,name='debit'),
    path('credit',credit,name='credit'),
]
