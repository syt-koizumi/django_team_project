# Generated by Django 5.0.6 on 2024-06-19 08:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("comment", "0004_alter_comment_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 6, 19, 17, 20, 10, 91004),
                verbose_name="投稿日",
            ),
        ),
    ]