# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-01 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20170601_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dessert_shop',
            name='shopid',
            field=models.IntegerField(max_length=100),
        ),
    ]