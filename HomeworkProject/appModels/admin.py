from django.contrib import admin
from . import models


class UserGroupInline(admin.TabularInline):
    model = models.UserGroup
    extra = 0
    autocomplete_fields = ('user',)


class HomeworkInline(admin.StackedInline):
    model = models.Homework
    extra = 0

@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = (UserGroupInline, HomeworkInline)
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)
    list_per_page = 20


@admin.register(models.UserGroup)
class UserGroupAdmin(admin.ModelAdmin):
    list_display = ('user', 'group')
    list_display_links = ('user', 'group')
    search_fields = ('user__username', )
    list_per_page = 20


class FileHomeworkInline(admin.TabularInline):
    model = models.FileHomework
    extra = 0

@admin.register(models.Homework)
class HomeworkAdmin(admin.ModelAdmin):
    inlines = (FileHomeworkInline, )
    list_display = ('title', 'group__title')
    list_display_links = ('title', 'group__title')
    search_fields = ('title', 'group__title')
    list_per_page = 20

@admin.register(models.FileHomework)
class FileHomeworkAdmin(admin.ModelAdmin):
    list_display = ('homework', 'file')
    list_display_links = ('homework', 'file')
    search_fields = ('homework__title', 'file')
    list_per_page = 20

