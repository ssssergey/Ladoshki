# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-04 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20160703_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_caption',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size_max',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size_min',
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
