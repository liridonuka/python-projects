from django.shortcuts import render
from django.views.generic import (View, TemplateView)
from django.http import HttpResponse

# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = 'layers/index.html'
