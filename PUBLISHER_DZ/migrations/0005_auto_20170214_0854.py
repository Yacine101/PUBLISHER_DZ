# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-02-14 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PUBLISHER_DZ', '0004_auto_20170212_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='e_mail',
            field=models.CharField(default='null', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='phone',
            field=models.CharField(default='null', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.CharField(max_length=50),
        ),
    ]
