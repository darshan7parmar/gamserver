# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-05 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameserverapp', '0004_auto_20160905_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='players',
            field=models.ManyToManyField(related_name='player', to='gameserverapp.Player'),
        ),
    ]
