# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cerandi_app', '0005_auto_20151117_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='advisor',
            name='plz_location',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='client',
            name='plz_location',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='client',
            name='watchlist',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='match',
            name='advisor',
            field=models.OneToOneField(to='cerandi_app.Advisor'),
        ),
        migrations.AddField(
            model_name='match',
            name='client',
            field=models.OneToOneField(to='cerandi_app.Client'),
        ),
    ]
