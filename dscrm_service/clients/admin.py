from django.contrib import admin

from .models import Client


class ClientAdmin(admin.ModelAdmin):
    search_fields = ('client_name', 'client_phone')
    list_display = ('id', 'client_name', 'client_phone')


admin.site.register(Client, ClientAdmin)
