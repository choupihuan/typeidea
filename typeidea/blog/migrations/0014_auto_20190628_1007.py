# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-28 02:07
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20190628_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(help_text='正文必须为MarkDown格式', verbose_name='正文'),
        ),
    ]
