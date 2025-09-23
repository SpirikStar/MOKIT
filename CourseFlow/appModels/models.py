from django.db import models


class Course(models.Model):
    title = models.CharField(
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание', 
        null=True, blank=True
    )
    status = models.BooleanField(
        verbose_name='Статус', 
        choices=[
            (True, 'Опубликован'),
            (False, 'Не опубликовано'),
        ],
        default=True
    )
    date_created = models.DateField(
        verbose_name='Дата создания', 
        auto_now_add=True
    )

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'Курсы'


class Topic(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='Курс'
    )
    title = models.CharField(
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание', 
        null=True, blank=True
    )
    status = models.BooleanField(
        verbose_name='Статус', 
        choices=[
            (True, 'Опубликован'),
            (False, 'Не опубликовано'),
        ],
        default=True
    )

    class Meta:
        verbose_name = 'тему'
        verbose_name_plural = 'Темы'


class SubTopic(models.Model):
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        verbose_name="Тема"
    )
    title = models.CharField(
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание",
        null=True,
        blank=True
    )
    status = models.BooleanField(
        verbose_name='Статус', 
        choices=[
            (True, 'Опубликован'),
            (False, 'Не опубликовано'),
        ],
        default=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'подтему'
        verbose_name_plural = 'Подтемы'
        # python manage.py makemigrations
        # python manage.py migrate
