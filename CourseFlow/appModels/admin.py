from django.contrib import admin
from .models import Course, Topic, SubTopic


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


class SubTopicInline(admin.StackedInline):
    model = SubTopic
    extra = 0

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    inlines = [SubTopicInline]
    autocomplete_fields = ['course']

    list_display = ['course', 'title', 'status']
    list_display_links = ['course', 'title', 'status']
    search_fields = ['title', 'description']
    list_filter = ['status', 'course']

    list_per_page = 20

@admin.register(SubTopic)
class SubTopicAdmin(admin.ModelAdmin):
    autocomplete_fields = ['topic']

    list_display = ['title', 'status']
    list_display_links = ['title', 'status']
    search_fields = ['title', 'description']
    list_filter = ['status']

    list_per_page = 20


