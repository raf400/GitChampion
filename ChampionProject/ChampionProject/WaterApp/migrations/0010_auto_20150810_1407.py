# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WaterApp', '0009_auto_20150810_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('username', models.CharField(max_length=12, serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=15)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='password',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='user',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='username',
        ),
        migrations.AddField(
            model_name='accounts',
            name='refills',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accounts',
            name='id',
            field=models.CharField(max_length=12, serialize=False, primary_key=True),
        ),
    ]
