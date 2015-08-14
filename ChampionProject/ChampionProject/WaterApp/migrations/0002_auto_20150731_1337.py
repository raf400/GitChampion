# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WaterApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=100, choices=[('student', 'Student'), ('teacher', 'Teacher')])),
            ],
        ),
        migrations.AddField(
            model_name='accounts',
            name='password',
            field=models.CharField(default=b'', max_length=12),
        ),
    ]
