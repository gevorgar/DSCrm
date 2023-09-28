from django import forms
from .models import Client

class ClientCreateForm(forms.ModelForm):
   class Meta:
       model = Client
       fields = ('client_name', 'client_phone', 'reklam_company')
       widgets = {
           'client_name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
           'client_phone': forms.NumberInput(attrs={'class': 'form-control', 'type': 'text'}),
           'reklam_company': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
       }