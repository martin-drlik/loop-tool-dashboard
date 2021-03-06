# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 04:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DimDate',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('date_day', models.IntegerField()),
                ('date_year', models.IntegerField()),
                ('date_month', models.IntegerField()),
                ('date_dayinweek', models.IntegerField()),
                ('date_week', models.IntegerField()),
                ('unixtimestamp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DimPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.CharField(max_length=255)),
                ('content_id', models.IntegerField()),
                ('parent_id', models.IntegerField(default=0)),
                ('order_no', models.IntegerField(default=0)),
                ('title', models.TextField()),
                ('page_pk', models.CharField(max_length=255)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Course')),
            ],
        ),
        migrations.CreateModel(
            name='DimSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.IntegerField()),
                ('unixtimestamp', models.IntegerField()),
                ('date_id', models.CharField(max_length=255)),
                ('session_length_in_mins', models.IntegerField()),
                ('pageviews', models.IntegerField()),
                ('date_year', models.IntegerField()),
                ('date_week', models.IntegerField()),
                ('date_dayinweek', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Course')),
            ],
        ),
        migrations.CreateModel(
            name='DimSubmissionAttempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('grade', models.CharField(max_length=50)),
                ('unixtimestamp', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Course')),
            ],
        ),
        migrations.CreateModel(
            name='DimSubmissionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_id', models.IntegerField()),
                ('content_type', models.CharField(max_length=255)),
                ('timeopen', models.CharField(max_length=255)),
                ('timeclose', models.CharField(max_length=255)),
                ('grade', models.CharField(max_length=50)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Course')),
            ],
        ),
        migrations.CreateModel(
            name='DimUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lms_id', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('user_pk', models.CharField(max_length=255)),
                ('firstname', models.CharField(blank=True, max_length=255)),
                ('lastname', models.CharField(blank=True, max_length=255)),
                ('role', models.CharField(blank=True, max_length=255)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Course')),
            ],
        ),
        migrations.CreateModel(
            name='FactCourseVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_id', models.CharField(max_length=255)),
                ('user_id', models.IntegerField()),
                ('page_id', models.IntegerField()),
                ('pageview', models.IntegerField(default=1)),
                ('time_id', models.CharField(max_length=255)),
                ('module', models.CharField(blank=True, max_length=255)),
                ('action', models.CharField(blank=True, max_length=255)),
                ('url', models.TextField(blank=True)),
                ('section_id', models.IntegerField(blank=True, null=True)),
                ('user_pk', models.CharField(blank=True, max_length=255)),
                ('page_pk', models.CharField(blank=True, max_length=255)),
                ('section_pk', models.CharField(blank=True, max_length=255)),
                ('unixtimestamp', models.IntegerField()),
                ('section_order', models.IntegerField(blank=True, null=True)),
                ('info', models.TextField()),
                ('session_id', models.IntegerField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Course')),
            ],
        ),
        migrations.CreateModel(
            name='SummaryCourseAssessmentVisitsByDayInWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_year', models.IntegerField()),
                ('date_day', models.IntegerField()),
                ('date_week', models.IntegerField()),
                ('date_dayinweek', models.IntegerField()),
                ('pageviews', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Course')),
            ],
        ),
        migrations.CreateModel(
            name='SummaryCourseCommunicationVisitsByDayInWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_year', models.IntegerField()),
                ('date_day', models.IntegerField()),
                ('date_week', models.IntegerField()),
                ('date_dayinweek', models.IntegerField()),
                ('pageviews', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Course')),
            ],
        ),
        migrations.CreateModel(
            name='SummaryCourseVisitsByDayInWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_year', models.IntegerField()),
                ('date_day', models.IntegerField()),
                ('date_week', models.IntegerField()),
                ('date_dayinweek', models.IntegerField()),
                ('pageviews', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Course')),
            ],
        ),
        migrations.CreateModel(
            name='SummaryDiscussion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forum_id', models.IntegerField()),
                ('title', models.TextField()),
                ('no_posts', models.IntegerField()),
                ('sna_json', models.TextField()),
                ('discussion_id', models.IntegerField()),
                ('forum_pk', models.CharField(max_length=255)),
                ('discussion_pk', models.CharField(max_length=255)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Course')),
            ],
        ),
        migrations.CreateModel(
            name='SummaryForum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forum_id', models.IntegerField()),
                ('title', models.TextField()),
                ('no_discussions', models.IntegerField()),
                ('forum_pk', models.CharField(max_length=255)),
                ('all_content', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Course')),
            ],
        ),
        migrations.CreateModel(
            name='SummaryParticipatingUsersByDayInWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_year', models.IntegerField()),
                ('date_day', models.IntegerField()),
                ('date_week', models.IntegerField()),
                ('date_dayinweek', models.IntegerField()),
                ('pageviews', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Course')),
            ],
        ),
        migrations.CreateModel(
            name='SummaryPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_id', models.CharField(max_length=255)),
                ('forum_id', models.IntegerField()),
                ('discussion_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Course')),
            ],
        ),
        migrations.CreateModel(
            name='SummarySessionAverageLengthByDayInWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_year', models.IntegerField()),
                ('date_week', models.IntegerField()),
                ('date_dayinweek', models.IntegerField()),
                ('session_average_in_minutes', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Course')),
            ],
        ),
        migrations.CreateModel(
            name='SummarySessionAveragePagesPerSessionByDayInWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_year', models.IntegerField()),
                ('date_week', models.IntegerField()),
                ('date_dayinweek', models.IntegerField()),
                ('pages_per_session', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Course')),
            ],
        ),
        migrations.CreateModel(
            name='SummarySessionsByDayInWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_year', models.IntegerField()),
                ('date_week', models.IntegerField()),
                ('date_dayinweek', models.IntegerField()),
                ('sessions', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Course')),
            ],
        ),
        migrations.CreateModel(
            name='SummaryUniquePageViewsByDayInWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_year', models.IntegerField()),
                ('date_day', models.IntegerField()),
                ('date_week', models.IntegerField()),
                ('date_dayinweek', models.IntegerField()),
                ('pageviews', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Course')),
            ],
        ),
    ]
