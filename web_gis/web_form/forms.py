from django import forms
from web_form.models import Contact
from django.core import validators

def check_for_z(value):
    if len(value) > 15:
        raise forms.ValidationError("Name cannot contain more then 15 chars")

class AddValues(forms.ModelForm):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Verify you email')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                #following, prevent from bot using method from core
                                validators=[validators.MaxLengthValidator(0)])
    class Meta():
        model = Contact
        fields = '__all__'

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        verify_email = all_clean_data['verify_email']

        if email != verify_email:
            raise forms.ValidationError('Check if email and verify email are same')


#BAsic method to prevent from bot
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher):
    #         raise forms.ValidationError('I got you')
    #     return botcatcher
