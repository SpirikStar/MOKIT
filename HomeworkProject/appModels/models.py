from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    title = models.CharField(
        verbose_name='Название'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'группу'
        verbose_name_plural = 'Группы'

class UserGroup(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        verbose_name='Группа'
    )
    def __str__(self):
        return f'{self.user.username} - {self.group.title}'
    
    class Meta:
        verbose_name = 'связь'
        verbose_name_plural = 'Пользователи в группах'


class Homework(models.Model):
    title = models.CharField(
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True
    )
    status = models.BooleanField(
        verbose_name="Статус публикации",
        default=True
    )
    dtime_created = models.DateTimeField(
        verbose_name="Дата и время создания",
        auto_now_add=True
    )
    dtime_edit = models.DateTimeField(
        verbose_name="Дата и время изменения",
        auto_now=True
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        verbose_name='Группа'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'домашнее задание'
        verbose_name_plural = 'Домашние задания'


class FileHomework(models.Model):
    file = models.FileField(
        verbose_name='Файл'
    )
    homework = models.ForeignKey(
        Homework,
        on_delete=models.CASCADE,
        verbose_name='Домашнее задание'
    )
    def __str__(self):
        return self.homework.title
    
    class Meta:
        verbose_name = 'файл'
        verbose_name_plural = 'Файлы'