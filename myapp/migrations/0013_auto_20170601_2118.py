# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-01 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20170601_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dessert',
            name='id',
        ),
        migrations.RemoveField(
            model_name='dessert_shop',
            name='shopid',
        ),
        migrations.AddField(
            model_name='dessert',
            name='dessertid',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
