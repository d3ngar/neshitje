# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_track', '0003_auto_20150905_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cookietracker',
            name='date_added',
            field=models.DateTimeField(verbose_name=b'Date Created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sessiontracker',
            name='session_start',
            field=models.DateTimeField(verbose_name=b'Date time created'),
            preserve_default=True,
        ),
    ]
