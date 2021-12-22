# Generated by Django 3.2.10 on 2021-12-22 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='No name', max_length=100)),
                ('description', models.TextField(blank=True, default='No description')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
