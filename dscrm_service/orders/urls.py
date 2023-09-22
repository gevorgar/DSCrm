from django.urls import path

from .views import *

urlpatterns = [
    path('', OrderList.as_view(), name='orders' ),
    path('create/', create_order, name='order_create'),
    path('<int:order_id>/', ShowOrder.as_view(), name='order')
]