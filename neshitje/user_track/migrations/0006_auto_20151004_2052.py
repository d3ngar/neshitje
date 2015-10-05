# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_track', '0005_auto_20151004_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cookietracker',
            name='session_owner',
        ),
        migrations.AddField(
            model_name='sessiontracker',
            name='session_owner',
            field=models.IntegerField(null=True, verbose_name=django.contrib.auth.models.User, blank=True),
            preserve_default=True,
        ),
    ]
