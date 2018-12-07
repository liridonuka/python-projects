from django.shortcuts import render
from django.views.generic import View, TemplateView,ListView,DetailView
from . import models

# # Create your views here.
# class IndexView(TemplateView):
#     template_name = 'index.html'

class DepartmentListView(ListView):
    context_object_name = 'departments'
    model =  models.Department

class DepartmentDetailView(DetailView):
    context_object_name = 'department_detail'
    model = models.Department
    #template_name = 'org_app/department_detail.html'
