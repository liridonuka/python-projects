#from django.conf.urls import url
from django.urls import path
from map_app import views

urlpatterns = [
    path('',views.index, name='mapapp'),
]
