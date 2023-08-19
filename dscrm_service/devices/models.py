from django.db import models

class Device(models.Model):
    """Устройство"""

    class Meta:
        db_table = "devices"
        verbose_name = "Устройство"
        verbose_name_plural = "Устройства"

    group = models.CharField(verbose_name="Группа")
    brand = models.CharField(verbose_name="Бренд")
    model = models.CharField(verbose_name="Модель")


    def __str__(self):
        return f"{self.brand} {self.model}"

class DeviceInField(models.Model):
    """Добавляемые устройства"""

    class Meta:
        db_table = "devices_in_fields"
        verbose_name = "Добавляемое устройство"
        verbose_name_plural = "Добавляемые устройства"

    serial_number = models.TextField(verbose_name="Серийный номер", unique=True)
    device = models.ForeignKey(Device, on_delete=models.RESTRICT, verbose_name="Устройство")


    def __str__(self):
        return f"{self.device} с/н {self.serial_number}"