from django.db import models

class Click(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name="IP Адрес")
    browser_info = models.TextField(verbose_name="Информация о браузере")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Время клика")
    project = models.SlugField(verbose_name="Проект", default='default')

    def __str__(self):
        return f"{self.ip_address} - {self.timestamp}"