# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WaterApp', '0011_remove_staff_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='refills',
        ),
    ]
