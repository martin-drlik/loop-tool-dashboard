# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 03:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='owner',
            new_name='owners',
        ),
    ]