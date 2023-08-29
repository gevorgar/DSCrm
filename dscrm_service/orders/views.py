from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *


def view_orders(request):
    orders = Order.objects.all()
    return render(request, 'orders/orders.html', {'orders': orders, 'title': 'Таблица заявок'})


def create_order(request):
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('orders')
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create_order.html', {'form': form, 'title': 'Создание заявки'})

def edit_order(request, order_id):
    return HttpResponse(f'Редактирование заявки {order_id}')