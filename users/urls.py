from django.views.generic.base import TemplateView
from django.urls import path
from .views import SignUpView,UserDetailView
urlpatterns=[
    path('signup/',SignUpView.as_view(),name='signup'),
    path('detail/',UserDetailView.as_view(),name='customerdetail'),
    path('',TemplateView.as_view(template_name='customer.html'),name='customer'),

]
