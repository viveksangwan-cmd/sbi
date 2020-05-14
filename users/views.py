from django.shortcuts import render,get_object_or_404
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


class UserDetailView(DetailView):
    model=CustomUser
    template_name='customerDetail.html'


    def get_object(self):
        return self.request.user
