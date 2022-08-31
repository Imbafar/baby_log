from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Record(models.Model):

    text = models.PositiveIntegerField("Сколько мл", help_text="Введите мл")
    pub_date = models.DateTimeField("Дата записи", default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="record", verbose_name="Автор"
    )
    kasha = models.BooleanField('Каша ли это?', default=False)

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return f"{self.text}"
