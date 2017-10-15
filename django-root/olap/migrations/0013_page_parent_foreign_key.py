# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 06:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('olap', '0012_rename_DimSubmissionType_to_SubmissionType'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='parent_id',
        ),
        migrations.AddField(
            model_name='page',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='olap.Page'),
        ),
    ]
