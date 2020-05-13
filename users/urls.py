from django.views.generic.base import TemplateView
from django.urls import path
from .views import SignUpView,UserDetailView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('signup/',SignUpView.as_view(),name='signup'),
    path('detail/',UserDetailView.as_view(),name='customerdetail'),
    path('',TemplateView.as_view(template_name='customer.html'),name='customer'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
