# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CookieTracker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(verbose_name=b'Date Created')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PageTracker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_stamp', models.DateTimeField(verbose_name=b'Date time created')),
                ('user_agent', models.CharField(max_length=1024)),
                ('ip_v4', models.CharField(max_length=14, null=True, blank=True)),
                ('ip_v6', models.CharField(max_length=46, null=True, blank=True)),
                ('ref_url', models.CharField(max_length=1024, null=True, blank=True)),
                ('source_id', models.IntegerField(null=True, blank=True)),
                ('page_count', models.IntegerField(default=0)),
                ('curr_url', models.CharField(max_length=200)),
                ('language_code', models.CharField(default=b'en-gb', max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SessionTracker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ref_url', models.CharField(max_length=1024)),
                ('session_start', models.DateTimeField(verbose_name=b'Date time created')),
                ('ip_v4', models.CharField(max_length=14)),
                ('ip_v6', models.CharField(max_length=46)),
                ('user_agent', models.CharField(max_length=1024)),
                ('country_code', models.CharField(max_length=3)),
                ('city', models.CharField(max_length=25)),
                ('mktg_trck_id', models.CharField(max_length=20)),
                ('language_code', models.CharField(max_length=3)),
                ('session_owner', models.IntegerField(null=True, verbose_name=django.contrib.auth.models.User, blank=True)),
                ('cookie', models.ForeignKey(to='user_track.CookieTracker')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SourceID',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source_name', models.CharField(max_length=60)),
                ('http_ref', models.CharField(max_length=80, null=True, blank=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Created', null=True)),
                ('status_changed', models.DateTimeField(auto_now=True, verbose_name=b'Date Created', null=True)),
                ('status', models.ForeignKey(default=1, to='main_app.Status')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='sessiontracker',
            name='source_id',
            field=models.ForeignKey(default=1, to='user_track.SourceID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagetracker',
            name='session',
            field=models.ForeignKey(to='user_track.SessionTracker'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cookietracker',
            name='source',
            field=models.ForeignKey(default=1, to='user_track.SourceID'),
            preserve_default=True,
        ),
    ]
