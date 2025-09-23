from django.contrib import admin
from .models import Course, Topic


class TopicInline(admin.StackedInline):
    model = Topic
    extra = 0

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [TopicInline]
    list_display = ['title', 'status', 'date_created']
    list_display_links = ['title', 'status']
    list_filter = ['status', 'date_created']
    search_fields = ['title', 'description']

    list_per_page = 20


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    autocomplete_fields = ['course']