# Generated by Django 5.0.6 on 2024-06-17 06:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="有効"),
        ),
    ]