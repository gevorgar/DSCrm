from django.urls import path

from .views import *

urlpatterns = [
    path('', view_orders, name='orders' ),
    path('create/', create_order, name='order_create'),
    path('<int:order_id>/', edit_order, name='order')
]