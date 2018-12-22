from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView,ListView,DetailView,
                                CreateView, DeleteView, UpdateView)
from . import models
from history_rec.mixes import ObjectViewedMix

# # Create your views here.
# class IndexView(TemplateView):
#     template_name = 'index.html'

class DepartmentListView(ListView):
    context_object_name = 'departments'
    model =  models.Department

class DepartmentDetailView(ObjectViewedMix,DetailView):
    context_object_name = 'department_detail'
    model = models.Department
    #template_name = 'org_app/department_detail.html'
class DepartmentCreateView(CreateView):
    fields = ('name','director')
    model = models.Department

class DepartmentUpdateView(ObjectViewedMix, UpdateView):
    fields = ('__all__')
    model = models.Department

class DepartmentDeleteView(DeleteView):
    model = models.Department
    success_url = reverse_lazy('org_app:list')
