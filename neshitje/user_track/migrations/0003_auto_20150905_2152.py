# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_track', '0002_auto_20150905_2138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pagetracker',
            old_name='session_id',
            new_name='session',
        ),
        migrations.RenameField(
            model_name='sessiontracker',
            old_name='cookie_id',
            new_name='cookie',
        ),
        migrations.RemoveField(
            model_name='cookietracker',
            name='cookie_id',
        ),
        migrations.RemoveField(
            model_name='sessiontracker',
            name='session_id',
        ),
    ]
