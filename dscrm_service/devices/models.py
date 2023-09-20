from django.db import models

class Group(models.Model):
    group = models.CharField(verbose_name="Группа", max_length=10)

    def __str__(self):
        return f"{self.group}"

class Brand(models.Model):
    brand = models.CharField(verbose_name="Бренд", max_length=10)

    def __str__(self):
        return f"{self.brand}"

class Model(models.Model):
    model = models.CharField(verbose_name="Модель", max_length=10)

    def __str__(self):
        return f"{self.model}"


class Device(models.Model):
    """Устройство"""

    class Meta:
        db_table = "devices"
        verbose_name = "Устройство"
        verbose_name_plural = "Устройства"

    group = models.ForeignKey(Group, on_delete=models.RESTRICT, verbose_name="Группа")
    brand = models.ForeignKey(Brand, on_delete=models.RESTRICT, verbose_name="Бренд")
    model = models.ForeignKey(Model, on_delete=models.RESTRICT, verbose_name="Модель")
    serial_number = models.TextField(verbose_name="Серийный номер",  blank=True)

    def __str__(self):
        return f"{self.model} {self.serial_number}"

# class DeviceInField(models.Model):
#     """Добавляемые устройства"""
#
#     class Meta:
#         db_table = "devices_in_fields"
#         verbose_name = "Добавляемое устройство"
#         verbose_name_plural = "Добавляемые устройства"
#
#     serial_number = models.TextField(verbose_name="Серийный номер", unique=True)
#     device = models.ForeignKey(Device, on_delete=models.RESTRICT, verbose_name="Устройство")
#
#
#     def __str__(self):
#         return f"{self.device} с/н {self.serial_number}"