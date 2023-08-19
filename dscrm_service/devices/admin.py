from django.contrib import admin

from models import Device, DeviceInField


class DeviceAdmin(admin.ModelAdmin):
    search_fields = ('brand', 'model')
    list_display = ('id', 'brand', 'model')

class DeviceInFieldAdmin(admin.ModelAdmin):
    search_fields = ('serial_number', 'device')
    list_display = ('id', 'device', 'serial_number')


admin.site.register(Device, DeviceAdmin)
admin.site.register(DeviceInField, DeviceInFieldAdmin)
