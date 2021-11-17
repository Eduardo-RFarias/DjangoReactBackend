from django.contrib import admin

from .models import Todo

# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = ('name', 'done', 'created_at')
    list_filter = ['created_at']
    search_fields = ['name']


admin.site.register(Todo, TodoAdmin)
