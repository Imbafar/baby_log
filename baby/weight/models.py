from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Weight(models.Model):

    amount = models.PositiveIntegerField("Сколько грамм", help_text="Введите вес в граммах")
    pub_date = models.DateTimeField("Дата записи", default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="weight", verbose_name="Автор"
    )

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "Вес"
        verbose_name_plural = "Вес"

    def __str__(self):
        return f"{self.amount}"
