from django.urls import path
from web_form import views

app_name = 'web_form'

urlpatterns = [
    path('',views.index, name='contacts'),
    path('add/',views.add_records,name='add_contact'),
]
