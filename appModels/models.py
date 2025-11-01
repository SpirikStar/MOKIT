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



class Service(models.Model):
    title = models.CharField(
        verbose_name="Название услуги"
    )
    
    # __str__ - встроенный метод класса, который определяет, какая колонка будет по умолчанию возращена при выводе объекта
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "услугу"
        verbose_name_plural = "Услуги"

class Order(models.Model):
    # ForeignKey - связь один ко многим.
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        # CASCADE - удалять все связанные записи. Пример: если удалить пользователя, то удаляться все его заказы
        on_delete=models.CASCADE
    )
    address = models.CharField(
        verbose_name="Адрес"
    )
    dtime = models.DateTimeField(
        verbose_name="Дата и время"
    )
    service = models.ForeignKey(
        Service,
        verbose_name="Услуга",
        on_delete=models.CASCADE
    )
    method_pay = models.CharField(
        verbose_name="Способ оплаты",
        max_length=120,
        # choices - список возможных вариантов. Вид [(запись в бд, отображение в интерфейсе)]
        choices=[
            ("Наличные", "Наличные"),
            ("Карта", "Карта")
        ],
        # default - значение по умолчанию
        default="Наличные"
    )
    status = models.CharField(
        verbose_name="Статус",
        max_length=120,
        # choices - список возможных вариантов. Вид [(запись в бд, отображение в интерфейсе)]
        choices=[
            ("В работе", "В работе"),
            ("Выполнено", "Выполнено"),
            ("Отменено", "Отменено")
        ],
        # default - значение по умолчанию
        default="В работе"
    )
    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "Заказы"