from django.shortcuts import render
from django.views.generic import (View, TemplateView,ListView)
from django.core.serializers import serialize
from django.http import HttpResponse
from layers import models
# Create your views here.

class MapTemplateView(TemplateView):
    template_name = 'map/index.html'

def religion_dataset(request):
    religion = serialize('geojson', models.Religion.objects.all())
    return HttpResponse(religion, content_type = 'json')

def citypark_dataset(request):
    citypark = serialize('geojson', models.CityPark.objects.all())
    return HttpResponse(citypark, content_type = 'json')
