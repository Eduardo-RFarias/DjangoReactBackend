from django.contrib import admin

from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ("name", "done", "created_at", "owner")
    list_filter = ["created_at"]
    search_fields = ["name"]


admin.site.register(Todo, TodoAdmin)
