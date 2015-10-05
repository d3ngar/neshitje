# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_track', '0006_auto_20151004_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='sourceid',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Date Created', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sourceid',
            name='status',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sourceid',
            name='status_changed',
            field=models.DateTimeField(auto_now=True, verbose_name=b'Date Created', null=True),
            preserve_default=True,
        ),
    ]
