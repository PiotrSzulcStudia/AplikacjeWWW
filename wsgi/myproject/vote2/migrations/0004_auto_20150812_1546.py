# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote2', '0003_auto_20150812_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('receivedCardsToVote', models.IntegerField(default=0)),
                ('votersAllowedToVote', models.IntegerField(default=0)),
                ('parentId', models.ForeignKey(to='vote2.District')),
            ],
        ),
        migrations.RemoveField(
            model_name='commision',
            name='parentId',
        ),
        migrations.DeleteModel(
            name='Commision',
        ),
    ]
