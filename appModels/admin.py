from django.contrib import admin
from appModels.models import User, Service, Order


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_display_links = ['first_name', 'last_name']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    # list_display - отображаемые поля
    list_display = ['title']

    # list_display_links - ссылки, которые открываются при нажатии
    list_display_links = ['title']

# admin.register() - регистрируем модель в админке


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'dtime', 'service', 'method_pay']
    list_display_links = ['user', 'address', 'dtime', 'service', 'method_pay']

    # list_filter - фильтры
    list_filter = ['dtime', 'service', 'method_pay']
