# Generated by Django 5.0.5 on 2024-06-24 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ThisWeekMovies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='映画名')),
                ('day', models.DateField(verbose_name='公開日')),
                ('youtube', models.TextField(max_length=10000, verbose_name='youtubeの埋め込みリンク')),
                ('overview', models.TextField(max_length=10000, verbose_name='映画概要')),
            ],
        ),
    ]
