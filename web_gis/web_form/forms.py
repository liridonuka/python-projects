from django import forms

class AddValues(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
