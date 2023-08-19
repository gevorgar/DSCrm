from django.contrib import admin

from models import Service, ServicePrice


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'warranty')

class PriceAdmin(admin.ModelAdmin):
    list_display = ['id','orders','price']


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServicePrice, PriceAdmin)
