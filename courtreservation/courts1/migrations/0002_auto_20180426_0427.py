# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-26 04:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courts1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loaded_team',
            old_name='court',
            new_name='court_id',
        ),
    ]
