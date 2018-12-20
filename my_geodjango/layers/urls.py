from django.urls import path
from layers import views

app_name = 'layers'

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='layers'),
]
