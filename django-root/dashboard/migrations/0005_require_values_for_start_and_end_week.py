# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_repeating_event_day_of_week_to_int'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courserepeatingevent',
            name='end_week',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='courserepeatingevent',
            name='start_week',
            field=models.IntegerField(),
        ),
    ]
