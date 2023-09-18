from django.contrib import admin

from .models import *


class DeviceAdmin(admin.ModelAdmin):
    search_fields = ('brand', 'model')
    list_display = ('id', 'brand', 'model')

class GroumAdmin(admin.ModelAdmin):
    list_display = ('group',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand',)

class ModelAdmin(admin.ModelAdmin):
    list_display = ('model',)

admin.site.register(Group, GroumAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Model, ModelAdmin)

admin.site.register(Device, DeviceAdmin)

