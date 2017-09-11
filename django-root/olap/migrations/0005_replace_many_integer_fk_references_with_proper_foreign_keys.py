# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 03:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('olap', '0004_replace_user_ids_with_DimUser_FKs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dimpage',
            name='page_pk',
        ),
        migrations.RemoveField(
            model_name='dimsession',
            name='session_id',
        ),
        migrations.RemoveField(
            model_name='dimsubmissionattempt',
            name='content_id',
        ),
        migrations.RemoveField(
            model_name='dimuser',
            name='user_pk',
        ),
        migrations.RemoveField(
            model_name='factcoursevisit',
            name='course',
        ),
        migrations.RemoveField(
            model_name='factcoursevisit',
            name='page_id',
        ),
        migrations.RemoveField(
            model_name='factcoursevisit',
            name='page_pk',
        ),
        migrations.RemoveField(
            model_name='factcoursevisit',
            name='pageview',
        ),
        migrations.RemoveField(
            model_name='factcoursevisit',
            name='session_id',
        ),
        migrations.RemoveField(
            model_name='factcoursevisit',
            name='user_pk',
        ),
        migrations.AddField(
            model_name='dimsubmissionattempt',
            name='page',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='olap.DimPage'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='factcoursevisit',
            name='page',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='olap.DimPage'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='factcoursevisit',
            name='session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='olap.DimSession'),
        ),
        migrations.AlterField(
            model_name='dimsession',
            name='first_visit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olap.FactCourseVisit'),
        ),
        migrations.AlterField(
            model_name='dimuser',
            name='email',
            field=models.EmailField(blank=True, max_length=255),
        ),
    ]
