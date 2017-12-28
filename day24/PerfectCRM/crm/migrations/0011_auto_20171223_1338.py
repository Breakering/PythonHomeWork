# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-23 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0010_auto_20171223_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='status',
            field=models.SmallIntegerField(choices=[(0, '未报名'), (1, '已报名'), (2, '毕业老学员')], default=0, verbose_name='报名状态'),
        ),
    ]
