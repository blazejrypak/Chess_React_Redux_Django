# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-06 10:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masterchess', '0002_auto_20180606_1026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='text',
            new_name='game_collation',
        ),
    ]
