from django.urls import path

from .views import *

urlpatterns = [
    path('', OrderList.as_view(), name='orders' ),
    path('create/', create_order, name='order_create'),
    path('<int:pk>/', OrderUpdate.as_view(), name='order'),

]