from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "cpf",
        "email",
        "full_name",
        "is_superuser",
        "date_joined",
        "is_active",
    )
    list_filter = ["date_joined"]
    search_fields = ["cpf", "email"]


admin.site.register(User, UserAdmin)
