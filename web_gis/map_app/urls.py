#from django.conf.urls import url
from django.urls import path
from map_app import views

app_name = 'map_app'

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:question_id>/',views.detail, name='details'),
]
