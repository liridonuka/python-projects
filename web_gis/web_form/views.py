from django.shortcuts import render
from . import forms
from web_form.models import Contact


def index(request):
    result = Contact.objects.order_by('name')
    contact_dict = {'contacts': result}
    return render(request,'web_form/index.html',context=contact_dict)

def add_records(request):
    form = forms.AddValues()

    if request.method == 'POST':
        form = forms.AddValues(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Duplicate values or Erros')

    return render(request,'web_form/add.html',{'form':form})
