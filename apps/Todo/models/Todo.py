from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Todo(models.Model):
    name = models.CharField(max_length=100, default="No name")
    description = models.TextField(blank=True, default="No description")
    created_at = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Name:{self.name} Created at:{self.created_at}"
