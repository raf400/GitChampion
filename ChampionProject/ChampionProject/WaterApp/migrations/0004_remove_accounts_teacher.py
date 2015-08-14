# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WaterApp', '0003_auto_20150805_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='teacher',
        ),
    ]
