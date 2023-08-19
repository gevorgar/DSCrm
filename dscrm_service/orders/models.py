from django.db import models
from datetime import datetime

from clients.models import Client
from devices.models import DeviceInField
from services.models import Service


class Order(models.Model):
    """Класс для создания заявки"""

    class Meta:
        db_table = "orders"
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    statuses = (("open", "открыта"),
                ("closed", "закрыта"),
                ("in progress", "в работе"),
                ("need info", "нужна информация"))

    client = models.ForeignKey(Client, on_delete=models.RESTRICT, verbose_name="Клиент")
    device = models.ForeignKey(DeviceInField, verbose_name="Устройство", on_delete=models.RESTRICT)
    order_description = models.TextField(verbose_name="Неисправность")
    created_dt = models.DateTimeField(verbose_name="Создано", auto_now_add=True)
    last_updated_dt = models.DateTimeField(verbose_name="Последнее изменение", blank=True, null=True)
    order_status = models.TextField(verbose_name="Статус заказа", choices=statuses)
    services = models.ManyToManyField(Service, through='ServicePrice', verbose_name="Услуга")

    def __str__(self):
        return f"Заявка №{self.id} для {self.device}"

    def save(self, *args, **kwargs):
        self.last_updated_dt = datetime.now()
        super().save(*args, **kwargs)