from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm,CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=CustomUser
    list_display=['Image','username','email','age','Firstname','Lastname','is_staff']

admin.site.register(CustomUser,CustomUserAdmin)
