from django.urls import path
from map import views

app_name = 'map'

urlpatterns = [
    path('',views.MapTemplateView.as_view(), name = 'map'),
    path('religion/', views.religion_dataset, name = 'religion'),
    path('citypark/', views.citypark_dataset, name = 'city_park'),
    path('layers/',views.layers_dataset, name = 'layers'),
    path('add/',views.add_religion, name = 'add'),
]
