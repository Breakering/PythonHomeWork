# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-16 08:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('password', models.CharField(help_text="<a href='password/'>点我修改密码</a>", max_length=128, verbose_name='password')),
                ('name', models.CharField(max_length=32)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name_plural': '账户表',
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='校区名称')),
                ('addr', models.CharField(max_length=128, verbose_name='校区地址')),
            ],
            options={
                'verbose_name_plural': '校区表',
            },
        ),
        migrations.CreateModel(
            name='ClassList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_type', models.SmallIntegerField(choices=[(0, '面授(脱产)'), (1, '面授(周末)'), (2, '网络班')], verbose_name='班级类型')),
                ('semester', models.PositiveSmallIntegerField(verbose_name='学期')),
                ('start_date', models.DateField(verbose_name='开班日期')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='结业日期')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Branch', verbose_name='校区')),
            ],
            options={
                'verbose_name_plural': '班级表',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='课程名称')),
                ('price', models.PositiveSmallIntegerField(verbose_name='课程价格')),
                ('period', models.PositiveSmallIntegerField(verbose_name='周期(月)')),
                ('outline', models.TextField(verbose_name='课程大纲')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '课程表',
            },
        ),
        migrations.CreateModel(
            name='CourseRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_num', models.PositiveSmallIntegerField(verbose_name='第几节(天)')),
                ('has_homework', models.BooleanField(default=True, verbose_name='是否有作业')),
                ('homework_title', models.CharField(blank=True, max_length=128, null=True, verbose_name='作业标题')),
                ('homework_content', models.TextField(blank=True, null=True, verbose_name='作业内容')),
                ('outline', models.TextField(verbose_name='本节课程大纲')),
                ('date', models.DateField(auto_now_add=True, verbose_name='创建日期')),
                ('from_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ClassList', verbose_name='班级')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='老师')),
            ],
            options={
                'verbose_name_plural': '上课记录表',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, null=True, verbose_name='客户姓名')),
                ('qq', models.CharField(max_length=64, unique=True, verbose_name='客户QQ')),
                ('qq_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='qq名称')),
                ('phone', models.CharField(blank=True, max_length=64, null=True, verbose_name='手机号')),
                ('source', models.SmallIntegerField(choices=[(0, '转介绍'), (1, 'QQ'), (2, '官网'), (3, '百度推广'), (4, '51CTO'), (5, '知乎'), (6, '市场推广')], verbose_name='客户来源')),
                ('referral_from', models.CharField(blank=True, max_length=64, null=True, verbose_name='转介绍人QQ')),
                ('content', models.TextField(verbose_name='咨询详情')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('status', models.SmallIntegerField(choices=[(0, '未报名'), (1, '已报名')], default=0, verbose_name='报名状态')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('consult_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Course', verbose_name='咨询课程')),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='顾问')),
            ],
            options={
                'verbose_name_plural': '客户信息表',
            },
        ),
        migrations.CreateModel(
            name='CustomerFollowUP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='跟进内容')),
                ('intention', models.SmallIntegerField(choices=[(0, '2周内报名'), (1, '1个月内报名'), (2, '近期无报名计划'), (3, '已在其它机构报名'), (4, '已报名'), (5, '已拉黑')], verbose_name='客户意向')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='跟进时间')),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='跟进顾问')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Customer', verbose_name='跟进客户')),
            ],
            options={
                'verbose_name_plural': '客户跟进记录表',
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_agreed', models.BooleanField(default=False, verbose_name='学员已同意合同')),
                ('contract_approved', models.BooleanField(default=False, verbose_name='合同已审核')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='报名时间')),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='课程顾问')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Customer', verbose_name='学员')),
                ('enrolled_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ClassList', verbose_name='所报班级')),
            ],
            options={
                'verbose_name_plural': '报名表',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='菜单名')),
                ('url_type', models.SmallIntegerField(choices=[(0, 'relative_name'), (1, 'absolute_url')], verbose_name='菜单url类型')),
                ('url_name', models.CharField(max_length=128, unique=True, verbose_name='菜单url')),
            ],
            options={
                'verbose_name_plural': '动态菜单表',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=500, verbose_name='缴费数额')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='缴费时间')),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='课程顾问')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Course', verbose_name='所报课程')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Customer', verbose_name='客户')),
            ],
            options={
                'verbose_name_plural': '缴费记录表',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='角色名称')),
                ('menus', models.ManyToManyField(blank=True, to='crm.Menu', verbose_name='菜单')),
            ],
            options={
                'verbose_name_plural': '角色表',
            },
        ),
        migrations.CreateModel(
            name='StudyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.SmallIntegerField(choices=[(0, '已签到'), (1, '迟到'), (2, '缺勤'), (3, '早退')], verbose_name='状态')),
                ('score', models.SmallIntegerField(choices=[(100, 'A+'), (90, 'A'), (85, 'B+'), (80, 'B'), (75, 'B-'), (70, 'C+'), (60, 'C'), (40, 'C-'), (-50, 'D'), (-100, 'COPY'), (0, 'N/A')], default=0, verbose_name='成绩')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('date', models.DateField(auto_now_add=True, verbose_name='创建日期')),
                ('course_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.CourseRecord', verbose_name='上课记录')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Enrollment', verbose_name='学生')),
            ],
            options={
                'verbose_name_plural': '学习记录表',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='标签名称')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '标签表',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='tags',
            field=models.ManyToManyField(blank=True, to='crm.Tag', verbose_name='标签'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Course', verbose_name='课程'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='teachers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='老师'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='roles',
            field=models.ManyToManyField(blank=True, default=None, to='crm.Role', verbose_name='所属角色'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterUniqueTogether(
            name='studyrecord',
            unique_together=set([('student', 'course_record')]),
        ),
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together=set([('customer', 'enrolled_class')]),
        ),
        migrations.AlterUniqueTogether(
            name='courserecord',
            unique_together=set([('from_class', 'day_num')]),
        ),
        migrations.AlterUniqueTogether(
            name='classlist',
            unique_together=set([('branch', 'course', 'semester')]),
        ),
    ]