from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .forms import *


class OrderList(ListView):
    model = Order
    template_name = 'orders/orders.html'
    context_object_name = 'orders'
    extra_context = {'title': 'Таблица заявок'}


class ShowOrder(DetailView):
    model = Order
    template_name = 'orders/order_info.html'
    pk_url_kwarg = 'order_id'
    context_object_name = 'order'


class CreateOrder(CreateView):
    form_class = OrderCreateForm
    template_name = 'orders/create_order.html'
    extra_context = {'title': 'Создание Заявки'}
    success_url = reverse_lazy('orders')



