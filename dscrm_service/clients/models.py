from django.db import models

class Client(models.Model):
    """Клиент"""

    class Meta:
        db_table = "clients"
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    client_name = models.CharField(verbose_name="Имя клиента", max_length=10)
    client_phone = models.CharField(verbose_name="Телефон", max_length=15)
    reklam_company = models.CharField(verbose_name="Рекламная компания", max_length=20, blank=True)

    def __str__(self):
        return f"{self.client_name} Телефон: {self.client_phone}"
