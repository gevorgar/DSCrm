from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .forms import ClientCreateForm
from .models import Client

class ClientList(ListView):
    model = Client
    template_name = 'clients/clients.html'
    context_object_name = 'clients'
    extra_context = {'title': 'Список клиентов'}

class ShowClient(DetailView):
    model = Client
    template_name = 'clients/client_info.html'
    pk_url_kwarg = 'client_id'
    context_object_name = 'client'

class AddClient(CreateView):
    form_class = ClientCreateForm
    template_name = 'clients/add_client.html'
    extra_context = {'title': 'Добавление клиента'}
    success_url = reverse_lazy('clients')