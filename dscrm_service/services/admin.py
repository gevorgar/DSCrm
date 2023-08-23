from django.contrib import admin

from .models import Service, ServicePrice


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'warranty')

class ServicePriceAdmin(admin.ModelAdmin):
    list_display = ['id','order','price']


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServicePrice, ServicePriceAdmin)
