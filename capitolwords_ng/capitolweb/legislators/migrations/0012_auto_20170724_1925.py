# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-24 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legislators', '0011_auto_20170724_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]