# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-16 08:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='c_name',
            new_name='client_name',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='c_phone',
            new_name='client_phone',
        ),
    ]
