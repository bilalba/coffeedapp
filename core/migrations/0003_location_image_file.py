# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 11:39
from __future__ import unicode_literals

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160715_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='image_file',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.upload_to_location),
        ),
    ]
