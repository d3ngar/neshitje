# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_track', '0003_auto_20151108_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessiontracker',
            name='language_code',
            field=models.CharField(max_length=6),
            preserve_default=True,
        ),
    ]
