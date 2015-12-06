# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0003_auto_20151123_0024'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeDenomination',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('denomination', models.IntegerField(null=True, blank=True)),
                ('attribute', models.ForeignKey(to='listing.Attribute')),
            ],
        ),
        migrations.CreateModel(
            name='ListingType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('listing_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='attributechoices',
            old_name='choice_numer',
            new_name='choice_number',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='condition',
        ),
        migrations.DeleteModel(
            name='Condition',
        ),
        migrations.AddField(
            model_name='attributedenomination',
            name='listing',
            field=models.ForeignKey(to='listing.Listing'),
        ),
        migrations.AddField(
            model_name='listing',
            name='listing_type',
            field=models.ForeignKey(default=1, to='listing.ListingType'),
            preserve_default=False,
        ),
    ]
