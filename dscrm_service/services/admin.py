from django.contrib import admin

from .models import Service, ServiceItem


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'warranty')


class ServiceItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'price']


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceItem, ServiceItemAdmin)
