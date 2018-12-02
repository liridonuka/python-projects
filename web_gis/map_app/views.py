from django.shortcuts import render
from django.http import HttpResponse
from map_app.models import Komuna, Vendi

# Create your views here.

def index(request):
    result = Komuna.objects.order_by('id_komuna')
    #result = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright", max_zoom = 4)
    komuna_dict = {'komuna_records':result}
    return render(request,'map_app/index.html',context=komuna_dict)

def detail(request, question_id):
    details={'insert_detail':'Te paraqitura ne detaje numri: ' + str(question_id)}
    return render(request,'map_app/detail.html',context=details)
