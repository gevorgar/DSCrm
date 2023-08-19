from django.db import models

class Client(models.Model):
    """Клиент"""

    class Meta:
        db_table = "clients"
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    client_name = models.CharField(verbose_name="Имя клиента")
    client_phone = models.TextField(verbose_name="Телефон")
    reklam_company = models.CharField(verbose_name="Рекламная компания")

    def __str__(self):
        return f"{self.client_name} Телефон: {self.client_phone}"
