from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "cpf",
        "email",
        "full_name",
        "is_superuser",
        "last_login",
        "date_joined",
        "is_active",
    )
    list_filter = ["date_joined", "last_login"]
    search_fields = ["cpf", "email", "full_name"]


admin.site.register(User, UserAdmin)
