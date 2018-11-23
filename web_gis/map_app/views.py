from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    list = []
    for i in range(50):
        list.append("Hello World ")

    return HttpResponse(list)
