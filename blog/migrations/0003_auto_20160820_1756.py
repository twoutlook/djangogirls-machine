# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_brief'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='r03c3',
            field=models.CharField(default='', max_length=99),
        ),
        migrations.AddField(
            model_name='post',
            name='r03c4',
            field=models.CharField(default='', max_length=99),
        ),
        migrations.AddField(
            model_name='post',
            name='r03c5',
            field=models.CharField(default='', max_length=99),
        ),
        migrations.AddField(
            model_name='post',
            name='r03c6',
            field=models.CharField(default='', max_length=99),
        ),
        migrations.AddField(
            model_name='post',
            name='r03c7',
            field=models.CharField(default='', max_length=99),
        ),
    ]
