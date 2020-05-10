from django.shortcuts import render
from django.views.generic import TemplateView

class Balance(TemplateView):
    template_name='balance.html'
