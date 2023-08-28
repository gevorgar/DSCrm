from django.shortcuts import render
from django.http import HttpResponse



def view_orders(request):
    return HttpResponse('Таблица заявок ')


def create_order(request):
    return HttpResponse('Создание Заявки')

def edit_order(request, order_id):
    return HttpResponse(f'Редактирование заявки {order_id}')