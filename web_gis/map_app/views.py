from django.shortcuts import render
from django.http import HttpResponse
from map_app.models import Komuna, Vendi
import datetime

# Create your views here.
def index(request):
    result = Komuna.objects.order_by('id_komuna')
    #result = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright", max_zoom = 4)
    komuna_dict = {'komuna_records':result}
    return render(request,'map_app/index.html',context=komuna_dict)

def detail(request, question_id):
    viti_aktual = str(datetime.date.today().year)
    result = Komuna.objects.get(id_komuna = question_id)
    komuna_dict = {'komuna_details': result}
    return render(request,'map_app/details.html',komuna_dict)
