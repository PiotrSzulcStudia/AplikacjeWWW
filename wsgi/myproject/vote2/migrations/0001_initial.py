# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('receivedCardsToVote', models.IntegerField()),
                ('votersAllowedToVote', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('parentId', models.ForeignKey(to='vote2.District')),
            ],
        ),
        migrations.AddField(
            model_name='commision',
            name='parentId',
            field=models.ForeignKey(to='vote2.District'),
        ),
    ]
