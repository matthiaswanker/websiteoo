# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('user_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bank_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('logo_url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('user_name', models.CharField(max_length=255)),
                ('moral_ratio', models.IntegerField(default=0)),
                ('risk_ratio', models.IntegerField(default=0)),
                ('gender', models.CharField(default=b'm', max_length=200, choices=[(b'm', b'm'), (b'w', b'w')])),
            ],
            options={
                'ordering': ('user_name',),
            },
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client', models.OneToOneField(to='cerandi_app.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ticker', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='investment',
            name='stock',
            field=models.OneToOneField(to='cerandi_app.Stock'),
        ),
        migrations.AddField(
            model_name='advisor',
            name='bank',
            field=models.ForeignKey(to='cerandi_app.Bank'),
        ),
    ]
