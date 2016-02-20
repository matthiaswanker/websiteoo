# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cerandi_app', '0011_auto_20151117_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(blank=True)),
                ('author', models.BooleanField()),
                ('send_date', models.DateTimeField()),
                ('advisor', models.ForeignKey(to='cerandi_app.Advisor')),
                ('client', models.ForeignKey(to='cerandi_app.Client')),
            ],
        ),
        migrations.AddField(
            model_name='stock',
            name='chart_url',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
