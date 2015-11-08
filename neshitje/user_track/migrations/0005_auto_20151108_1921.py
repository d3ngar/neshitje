# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_track', '0004_auto_20151108_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessiontracker',
            name='session_owner',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
