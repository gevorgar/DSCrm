from django.urls import path

from .views import OrderList, create_order, ShowOrder, OrderUpdate, OrderDelete

urlpatterns = [
    path('', OrderList.as_view(), name='orders'),
    path('create/', create_order, name='order_create'),
    path('<int:pk>/', ShowOrder.as_view(), name='order'),
    path('<int:pk>/update', OrderUpdate.as_view(), name='order-update'),
    path('<int:pk>/delete', OrderDelete.as_view(), name='order-delete')
]
