# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 01:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kc_app', '0002_auto_20160724_1821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='punch_in',
            old_name='hr_start',
            new_name='hr_to_work',
        ),
        migrations.RenameField(
            model_name='punch_in',
            old_name='min_start',
            new_name='min_to_work',
        ),
    ]
