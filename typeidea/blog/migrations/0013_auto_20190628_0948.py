# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-28 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20190628_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(help_text='正文必须为MarkDown格式', verbose_name='正文'),
        ),
    ]