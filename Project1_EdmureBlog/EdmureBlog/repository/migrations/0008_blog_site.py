# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-10 00:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0007_auto_20170110_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='site',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
    ]