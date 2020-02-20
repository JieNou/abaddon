# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-08-13 12:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=256, unique=True)),
                ('value', models.CharField(default=b'n/a', max_length=256)),
                ('comments', models.CharField(default=b'n/a', max_length=256)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'settings',
            },
        ),
    ]