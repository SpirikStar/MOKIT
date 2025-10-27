from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(
        verbose_name="Номер телефона"
    )
    middle_name = models.CharField(
        verbose_name="Отчество",
        max_length=120,
        null=True,
        blank=True
    )

    class Meta:
        db_table = "users"
        verbose_name = "пользователя"
        verbose_name_plural = "Пользователи"