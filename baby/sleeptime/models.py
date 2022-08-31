from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class SLeepTime(models.Model):

    pub_date_start = models.DateTimeField("Дата записи", default=timezone.now)
    pub_date_end = models.DateTimeField("Дата записи", default=timezone.now)
    # amount = models.TimeField("Сколько спали")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sleeptime", verbose_name="Автор"
    )

    class Meta:
        ordering = ["-pub_date_start"]
        verbose_name = "Время сна"
        verbose_name_plural = "Время сна"

    def __str__(self):
        return f"{self.amount}"
