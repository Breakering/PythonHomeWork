# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-09 13:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0020_auto_20180109_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='account',
        ),
        migrations.AlterField(
            model_name='customer',
            name='consultant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='顾问'),
        ),
    ]
