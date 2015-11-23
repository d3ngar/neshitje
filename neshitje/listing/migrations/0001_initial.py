# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
from decimal import Decimal
from django.conf import settings
import listing.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attribute_name', models.CharField(max_length=100)),
                ('attribute_type', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AttributeChoices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=100)),
                ('choice_numer', models.IntegerField(null=True)),
                ('attribute', models.ForeignKey(to='listing.Attribute')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AttributeMapping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attribute', models.ForeignKey(to='listing.Attribute')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CategoryTree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(unique=True, max_length=100)),
                ('custom_order', models.IntegerField(null=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='sub_category', blank=True, to='listing.CategoryTree', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
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
            name='Listing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('listing_name', models.CharField(max_length=100)),
                ('supplier_id', models.CharField(max_length=75, null=True, blank=True)),
                ('listing_description', models.TextField()),
                ('price', models.DecimalField(default=Decimal('0.0000'), max_digits=20, decimal_places=4)),
                ('in_stock', models.IntegerField(default=1)),
                ('keywords', models.CharField(max_length=4000, null=True, blank=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Created', null=True)),
                ('status_changed', models.DateTimeField(auto_now=True, verbose_name=b'Date Created', null=True)),
                ('condition', models.ForeignKey(to='listing.Condition')),
                ('currency_code', models.ForeignKey(to='listing.Currency')),
                ('status', models.ForeignKey(default=1, to='main_app.Status')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ListingImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Created', null=True)),
                ('status_changed', models.DateTimeField(auto_now=True, verbose_name=b'Date Created', null=True)),
                ('image', models.ImageField(upload_to=listing.models.where_to_upload)),
                ('listing', models.ForeignKey(to='listing.Listing')),
                ('status', models.ForeignKey(default=1, to='main_app.Status')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='attributemapping',
            name='category',
            field=models.ForeignKey(to='listing.CategoryTree'),
            preserve_default=True,
        ),
    ]
