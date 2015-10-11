# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal
import product.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('condition_description', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('currency_code', models.CharField(max_length=3)),
                ('currency_symbol', models.CharField(max_length=5)),
                ('currency_name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=100)),
                ('supplier_id', models.CharField(max_length=75, null=True, blank=True)),
                ('product_description', models.TextField()),
                ('price', models.DecimalField(default=Decimal('0.0000'), max_digits=20, decimal_places=4)),
                ('status', models.IntegerField(default=1)),
                ('in_stock', models.IntegerField(default=1)),
                ('keywords', models.CharField(max_length=4000, null=True, blank=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Created', null=True)),
                ('status_changed', models.DateTimeField(auto_now=True, verbose_name=b'Date Created', null=True)),
                ('condition', models.ForeignKey(to='product.Condition')),
                ('currency_code', models.ForeignKey(to='product.Currency')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=1)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Created', null=True)),
                ('status_changed', models.DateTimeField(auto_now=True, verbose_name=b'Date Created', null=True)),
                ('image', models.ImageField(upload_to=product.models.where_to_upload)),
                ('product', models.ForeignKey(to='product.Product')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
