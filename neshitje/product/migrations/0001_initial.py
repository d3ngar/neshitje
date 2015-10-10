# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=100)),
                ('supplier_id', models.CharField(max_length=75)),
                ('product_description', models.TextField()),
                ('price', models.DecimalField(default=Decimal('0.0000'), max_digits=20, decimal_places=4)),
                ('status', models.IntegerField(default=1)),
                ('in_stock', models.IntegerField(default=1)),
                ('keywords', models.CharField(max_length=4000)),
                ('condition', models.CharField(max_length=20)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Created', null=True)),
                ('status_changed', models.DateTimeField(auto_now=True, verbose_name=b'Date Created', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
