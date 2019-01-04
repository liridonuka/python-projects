from django import forms
from .models import Religion, AllLayers

from leaflet.forms.fields import GeometryCollectionField

class AllLayersForm(forms.ModelForm):
    location = GeometryCollectionField()


    class Meta:
        model = AllLayers
        fields = ('name','location')
