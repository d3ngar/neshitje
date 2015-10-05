# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_track', '0004_auto_20150905_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cookietracker',
            name='source_id',
        ),
        migrations.AddField(
            model_name='cookietracker',
            name='session_owner',
            field=models.IntegerField(null=True, verbose_name=django.contrib.auth.models.User, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cookietracker',
            name='source',
            field=models.ForeignKey(default=1, to='user_track.SourceID'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sessiontracker',
            name='source_id',
            field=models.ForeignKey(default=1, to='user_track.SourceID'),
            preserve_default=True,
        ),
    ]
