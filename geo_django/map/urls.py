from django.urls import path

from map import views
from .views import point_datasets

app_name = 'map'

urlpatterns = [
    path('',views.HomePageView.as_view(), name='home'),
    path('point/',point_datasets, name='pointer'),
]
