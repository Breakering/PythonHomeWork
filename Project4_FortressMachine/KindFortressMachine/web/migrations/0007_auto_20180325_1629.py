# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-25 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20180325_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multitaskdetail',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'init'), (1, 'success'), (2, 'failed')], default=0, verbose_name='执行状态'),
        ),
    ]