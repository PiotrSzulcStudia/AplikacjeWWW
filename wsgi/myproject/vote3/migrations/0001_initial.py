# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('receivedCardsToVote', models.IntegerField(default=0)),
                ('votersAllowedToVote', models.IntegerField(default=0)),
                ('timesModificated', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('parentId', models.ForeignKey(to='vote3.District', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='commission',
            name='parentId',
            field=models.ForeignKey(to='vote3.District'),
        ),
    ]
