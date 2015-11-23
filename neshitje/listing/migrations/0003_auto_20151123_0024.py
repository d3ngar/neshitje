# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0002_auto_20151123_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorytree',
            name='custom_order',
            field=models.PositiveIntegerField(default=1),
            preserve_default=True,
        ),
    ]
