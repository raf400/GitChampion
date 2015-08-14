# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WaterApp', '0004_remove_accounts_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='password',
        ),
        migrations.AddField(
            model_name='accounts',
            name='user',
            field=models.OneToOneField(default=None, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
