from django import forms
from .models import *

class OrderCreateForm(forms.ModelForm):
   class Meta:
       model = Order
       fields = ('client', 'device', 'order_description', 'price')
       widgets = {
           'order_description': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
           'price': forms.NumberInput(attrs={'class': 'form-control', 'type': 'text'}),
       }