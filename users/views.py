from django.shortcuts import render,redirect
from django.views.generic import CreateView,DetailView
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.db import connection
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
class SignUpView():
    def signup_view(request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        return render(request, 'signup.html', {'form': form})

class UserDetailView(LoginRequiredMixin,DetailView):
    model=CustomUser
    template_name='customerDetail.html'
    login_url='home'

    def get_object(self):
        return self.request.user

@user_passes_test(lambda u: u.is_staff, login_url=reverse_lazy('login'))
class DeleteView(LoginRequiredMixin):
    def delete_user(request):
        context = {}
        print(request.user)
        try:
            u = CustomUser.objects.get(username=request.user)
            u.delete()
        except Exception as e:
            print(e)
            return render(request,'delete_account.html',{'Exception':e})
        return render(request,'accounts/delete_account_success.html')
