# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WaterApp', '0006_auto_20150807_1232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='id',
        ),
        migrations.AddField(
            model_name='staff',
            name='first_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='last_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='password',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='username',
            field=models.CharField(default='', max_length=12, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
