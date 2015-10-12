# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBilling',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name=b'Date time created')),
                ('is_active', models.BooleanField(default=True)),
                ('address_line_1', models.CharField(max_length=55, null=True, blank=True)),
                ('address_line_2', models.CharField(max_length=55, null=True, blank=True)),
                ('address_line_3', models.CharField(max_length=55, null=True, blank=True)),
                ('city', models.CharField(max_length=55, null=True, blank=True)),
                ('post_code', models.CharField(max_length=10, null=True, blank=True)),
                ('status_changed', models.DateTimeField(auto_now=True, verbose_name=b'Date time updated')),
                ('status', models.ForeignKey(default=1, to='main_app.Status')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name=b'Date time created')),
                ('status_changed', models.DateTimeField(auto_now=True, verbose_name=b'Date time updated')),
                ('phone_number', models.CharField(max_length=16, null=True, blank=True)),
                ('gender', models.CharField(max_length=50, null=True, blank=True)),
                ('marketing_optin', models.BooleanField(default=True)),
                ('status', models.ForeignKey(default=1, to='main_app.Status')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserShipping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address_line_1', models.CharField(max_length=55, null=True, blank=True)),
                ('address_line_2', models.CharField(max_length=55, null=True, blank=True)),
                ('address_line_3', models.CharField(max_length=55, null=True, blank=True)),
                ('city', models.CharField(max_length=55, null=True, blank=True)),
                ('post_code', models.CharField(max_length=10, null=True, blank=True)),
                ('address_nick', models.CharField(max_length=55, null=True, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name=b'Date time created')),
                ('is_active', models.BooleanField(default=True)),
                ('status_changed', models.DateTimeField(auto_now=True, verbose_name=b'Date time updated')),
                ('status', models.ForeignKey(default=1, to='main_app.Status')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
