# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0003_auto_20151005_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='is_active',
        ),
        migrations.AddField(
            model_name='userdetail',
            name='status',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
