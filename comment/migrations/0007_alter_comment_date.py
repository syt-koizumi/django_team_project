# Generated by Django 5.0.6 on 2024-06-24 01:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("comment", "0006_comment_likes_alter_comment_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 6, 24, 10, 49, 31, 370998),
                verbose_name="投稿日",
            ),
        ),
    ]