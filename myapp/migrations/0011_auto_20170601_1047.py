# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-01 02:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20170601_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dessert',
            name='dessertid',
        ),
        migrations.AddField(
            model_name='dessert',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
