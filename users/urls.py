from django.views.generic.base import TemplateView
from django.urls import path
from .views import *
urlpatterns=[
    path('signup/',SignUpView.as_view(),name='signup'),
    path('detail',customerdetail,name='customerdetail'),
    path('',TemplateView.as_view(template_name='customer.html'),name='customer'),

]
