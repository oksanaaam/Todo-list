from django.contrib import admin

from case.models import Tag, Task


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["created_time", "content", "deadline", "is_done"]
    list_filter = ["created_time"]
    search_fields = ["content"]
