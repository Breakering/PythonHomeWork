# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-16 08:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='合同名称')),
                ('content', models.TextField(verbose_name='合同内容')),
            ],
            options={
                'verbose_name_plural': '合同表',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='联系邮箱'),
        ),
        migrations.AddField(
            model_name='customer',
            name='person_id',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='身份证号'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='contract',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Contract'),
        ),
    ]
