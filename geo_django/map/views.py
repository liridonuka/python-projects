from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse

from point.models import Xhamia
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'map/index.html'

def point_datasets(request):
    point = serialize('geojson', Xhamia.objects.all())
    return HttpResponse(point, content_type='json')
