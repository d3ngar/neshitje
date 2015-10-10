# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0004_auto_20151005_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='usershipping',
            name='city',
            field=models.CharField(max_length=55, null=True, blank=True),
            preserve_default=True,
        ),
    ]
