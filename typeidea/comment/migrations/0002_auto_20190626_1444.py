# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-26 06:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='target',
            field=models.CharField(max_length=100, verbose_name='评论目标'),
        ),
    ]
