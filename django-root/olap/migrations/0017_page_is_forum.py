# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_unique_course_offering_code'),
        ('olap', '0016_merge_20171011_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='is_forum',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterUniqueTogether(
            name='page',
            unique_together=set([('course_offering', 'content_id', 'is_forum')]),
        ),
    ]