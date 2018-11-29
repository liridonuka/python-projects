from django.urls import path
from web_form import views

urlpatterns = [
    path('',views.index, name='Register'),
    path('add/',views.add_records,name='Add records'),
]
