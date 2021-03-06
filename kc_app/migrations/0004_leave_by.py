# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 01:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kc_app', '0003_auto_20160724_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave_By',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hr_in', models.IntegerField(default=0, verbose_name='Clock in hour')),
                ('min_in', models.IntegerField(default=0, verbose_name='Clock in minute')),
                ('hr_leave', models.IntegerField(default=0, verbose_name='Hour to leave')),
                ('min_leave', models.IntegerField(default=0, verbose_name='Min to leave')),
            ],
        ),
    ]
