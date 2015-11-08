# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_track', '0002_bot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessiontracker',
            name='city',
            field=models.CharField(max_length=25, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sessiontracker',
            name='country_code',
            field=models.CharField(max_length=3, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sessiontracker',
            name='ip_v6',
            field=models.CharField(max_length=46, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sessiontracker',
            name='mktg_trck_id',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sessiontracker',
            name='ref_url',
            field=models.CharField(max_length=1024, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sessiontracker',
            name='user_agent',
            field=models.CharField(max_length=1024, null=True, blank=True),
            preserve_default=True,
        ),
    ]
