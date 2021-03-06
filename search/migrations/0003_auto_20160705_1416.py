# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-05 11:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_searchterm_tracking_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='searchterm',
            options={'ordering': ['-search_date'], 'verbose_name': '\u041f\u043e\u0438\u0441\u043a\u043e\u0432\u044b\u0439 \u0437\u0430\u043f\u0440\u043e\u0441', 'verbose_name_plural': '\u041f\u043e\u0438\u0441\u043a\u043e\u0432\u044b\u0435 \u0437\u0430\u043f\u0440\u043e\u0441\u044b'},
        ),
        migrations.AlterField(
            model_name='searchterm',
            name='ip_address',
            field=models.GenericIPAddressField(verbose_name='IP-\u0430\u0434\u0440\u0435\u0441'),
        ),
        migrations.AlterField(
            model_name='searchterm',
            name='q',
            field=models.CharField(max_length=50, verbose_name='\u041f\u043e\u0438\u0441\u043a\u043e\u0432\u0430\u044f \u0444\u0440\u0430\u0437\u0430'),
        ),
        migrations.AlterField(
            model_name='searchterm',
            name='search_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u041a\u043e\u0433\u0434\u0430 \u0438\u0441\u043a\u0430\u043b\u0438'),
        ),
        migrations.AlterField(
            model_name='searchterm',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c'),
        ),
    ]
