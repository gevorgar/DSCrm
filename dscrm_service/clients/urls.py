from django.urls import path

from .views import *

urlpatterns = [
    path('', ClientList.as_view(), name='clients'),
    path('client_add/', AddClient.as_view(), name='add_client'),
    path('<int:client_id>/', ShowClient.as_view(), name='client')
]