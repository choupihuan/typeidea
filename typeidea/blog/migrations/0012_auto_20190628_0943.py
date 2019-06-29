# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-28 01:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default=1, help_text='正文必须为MarkDown格式', verbose_name='正文'),
        ),
    ]
