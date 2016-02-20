# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cerandi_app', '0006_auto_20151117_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='investment',
            name='weight',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='stock',
            name='index',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='index_id',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='industry',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='sap_id',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='sector',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='sector_id',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='ticker_name',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='wkn',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='ticker',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
