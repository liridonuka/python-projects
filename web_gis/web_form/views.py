from django.shortcuts import render
from . import forms


def index(request):
    result = {'insert_me': "Please go to 'add/' and fill the form"}
    return render(request,'web_form/index.html',context=result)

def add_records(request):
    form = forms.AddValues()

    if request.method == 'POST':
        form = forms.AddValues(request.POST)

        if form.is_valid():
            print("Validation Success!")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])

    return render(request,'web_form/add.html',{'form':form})
