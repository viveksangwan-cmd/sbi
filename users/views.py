from django.shortcuts import render
from django.views.generic import CreateView,DetailView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from .models import CustomUser
from django.db import connection
from django.contrib.auth.mixins import LoginRequiredMixin
class SignUpView(CreateView):
    form_class=CustomUserCreationForm
    success_url=reverse_lazy('login')
    template_name='signup.html'

def customerdetail(request):
    print(request.user.username,request.user.age,request.user.Lastname)
    return render(request,'customerDetail.html',
    {'username':request.user.username,'Firstname':request.user.Firstname,'Lastname':request.user.Lastname,'age':request.user.age,'Email_ID':request.user.Email_ID,
    })
