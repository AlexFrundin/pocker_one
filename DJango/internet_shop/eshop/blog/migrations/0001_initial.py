# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 17:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
                ('text', models.TextField(verbose_name='Пост')),
                ('slug', models.SlugField(max_length=1000, unique_for_date='date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
    ]