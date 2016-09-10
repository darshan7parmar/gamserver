# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-10 09:39
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameserverapp', '0014_game_turn_sequence'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grid', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1), size=None), null=True, size=None)),
                ('board_rows', models.IntegerField(default=15)),
                ('board_cols', models.IntegerField(default=15)),
                ('num_words', models.IntegerField(default=10)),
                ('words_list', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), size=None)),
            ],
        ),
        migrations.RemoveField(
            model_name='game',
            name='admin_player',
        ),
        migrations.RemoveField(
            model_name='game',
            name='current_player',
        ),
        migrations.RemoveField(
            model_name='game',
            name='players',
        ),
        migrations.DeleteModel(
            name='Game',
        ),
    ]
