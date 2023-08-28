from django.urls import path

from .views import *

urlpatterns = [
    path('', view_orders),
    path('create/', create_order),
    path('<int:order_id>/', edit_order)
]