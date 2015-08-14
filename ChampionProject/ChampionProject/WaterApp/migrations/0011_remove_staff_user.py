# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WaterApp', '0010_auto_20150810_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='user',
        ),
    ]
