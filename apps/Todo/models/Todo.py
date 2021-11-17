from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=100, default='No name')
    description = models.TextField(blank=True, default='No description')
    created_at = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return f'Name:{self.name} Created at:{self.created_at}'
