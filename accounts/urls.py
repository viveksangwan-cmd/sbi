from django.urls import path
from .views import Balance
urlpatterns=[
    path('balance/',Balance.as_view(),name='balance')
]
