# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-15 11:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='s_phone',
            new_name='supplier_contact',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='s_name',
            new_name='supplier_name',
        ),
    ]
