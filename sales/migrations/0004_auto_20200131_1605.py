# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-31 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_auto_20200130_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
