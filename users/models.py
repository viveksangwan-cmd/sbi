from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age=models.PositiveIntegerField(null=True,blank=True)
    unique_no=models.AutoField(primary_key=True)
