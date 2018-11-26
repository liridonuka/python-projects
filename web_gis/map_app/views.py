from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    result = {'insert_me':'Kjo po vjen nga views!'}
    return render(request,'map_app/index.html',context=result)

def detail(request, question_id):
    details={'insert_detail':'Te paraqitura ne detaje numri: ' + str(question_id)}
    return render(request,'map_app/detail.html',context=details)
