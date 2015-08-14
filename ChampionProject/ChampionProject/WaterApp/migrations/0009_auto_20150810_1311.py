# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WaterApp', '0008_auto_20150810_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='id',
            field=models.CharField(default=b'', max_length=12),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='username',
            field=models.CharField(max_length=12, serialize=False, primary_key=True),
        ),
    ]
