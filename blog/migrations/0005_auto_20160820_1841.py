# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160820_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='brief',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AddField(
            model_name='post',
            name='r04c3',
            field=models.CharField(default='', max_length=99),
        ),
        migrations.AddField(
            model_name='post',
            name='r04c4',
            field=models.CharField(default='', max_length=99),
        ),
        migrations.AddField(
            model_name='post',
            name='r04c5',
            field=models.CharField(default='', max_length=99),
        ),
        migrations.AddField(
            model_name='post',
            name='r04c6',
            field=models.CharField(default='', max_length=99),
        ),
        migrations.AddField(
            model_name='post',
            name='r04c7',
            field=models.CharField(default='', max_length=99),
        ),
    ]
