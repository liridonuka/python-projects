from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    result = {'insert_me':'Kjo po vjen nga views!'}
    return render(request,'map_app/index.html',context=result)
