# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorytree',
            name='custom_order',
            field=models.PositiveIntegerField(null=True),
            preserve_default=True,
        ),
    ]
