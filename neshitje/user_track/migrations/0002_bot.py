# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_track', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip_v4', models.CharField(max_length=16, null=True, blank=True)),
                ('ip_v6', models.CharField(max_length=45, null=True, blank=True)),
                ('user_agent', models.CharField(max_length=2050, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
