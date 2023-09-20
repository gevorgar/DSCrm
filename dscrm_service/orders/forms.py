from django import forms
from .models import *
from devices.models import *
from  clients.models import *

class OrderCreateForm(forms.ModelForm):
   class Meta:
       model = Order
       fields = ('client', 'device', 'order_description', 'price')
       widgets = {
           'order_description': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
           'price': forms.NumberInput(attrs={'class': 'form-control', 'type': 'text'}),
       }



class OrderForm(forms.Form):
    client_name = forms.CharField(label='Имя клиента', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'text'}))
    client_phone = forms.CharField(label='Номер телефона', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'text'}))
    device_group = forms.ModelChoiceField(empty_label='Выберите группу', label='Группа', queryset=Group.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control'}))
    device_brand = forms.ModelChoiceField(empty_label='Выберите бренд', label='Бренд', queryset=Brand.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control'}))
    device_model = forms.ModelChoiceField(empty_label='Выберите Модель', label='Модель', queryset=Model.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control'}))
    device_serial = forms.CharField(label='Серийный номер', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'text'}))
    order_description = forms.CharField(label='Неисправность', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'text'}))
    price = forms.CharField(label='Ориентировочная цена', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'text'}))

