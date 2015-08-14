# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WaterApp', '0014_auto_20150813_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='id',
            field=models.CharField(max_length=12, serialize=False, primary_key=True),
        ),
    ]
