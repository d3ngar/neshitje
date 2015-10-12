# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_name', models.CharField(max_length=b'50')),
                ('status_description', models.CharField(max_length=b'1000', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
