# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-29 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20170720_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]