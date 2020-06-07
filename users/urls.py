from django.views.generic.base import TemplateView
from django.urls import path
from .views import SignUpView,UserDetailView,delete_account
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('signup/',SignUpView.signup_view,name='signup'),
    path('detail/',UserDetailView.as_view(),name='customerdetail'),
    path('',TemplateView.as_view(template_name='customer.html'),name='customer'),
    path('Close_Account/',TemplateView.as_view(template_name='accounts/delete_account.html'),name='delete_account'),
    path('Close_Account/delete_account_now',delete_account,name='delete_account_now'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
