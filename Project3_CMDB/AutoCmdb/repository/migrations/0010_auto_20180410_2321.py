# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-10 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0009_auto_20180410_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(max_length=64, unique=True, verbose_name='用户名'),
        ),
    ]
