# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import user_track.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_track', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CookieTracker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cookie_id', models.CharField(max_length=40)),
                ('source_id', models.IntegerField(null=True, blank=True)),
                ('date_added', models.DateField(verbose_name=b'Date Created')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pagetracker',
            name='session_id',
            field=models.ForeignKey(default=2131, to='user_track.SessionTracker'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sessiontracker',
            name='session_id',
            field=models.CharField(default=12312, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pagetracker',
            name='ip_v4',
            field=models.CharField(max_length=14, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pagetracker',
            name='ip_v6',
            field=models.CharField(max_length=46, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pagetracker',
            name='ref_url',
            field=models.CharField(max_length=1024, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pagetracker',
            name='source_id',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sessiontracker',
            name='cookie_id',
            field=models.ForeignKey(to='user_track.CookieTracker'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sessiontracker',
            name='source_id',
            field=models.IntegerField(verbose_name=user_track.models.SourceID),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceid',
            name='http_ref',
            field=models.CharField(max_length=80, null=True, blank=True),
            preserve_default=True,
        ),
    ]
