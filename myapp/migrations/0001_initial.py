# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-26 00:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('commentid', models.IntegerField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=1000)),
                ('comment_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='dessert',
            fields=[
                ('dessertid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='dessert_shop',
            fields=[
                ('shopid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=12)),
                ('order_sum', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('orderid', models.AutoField(primary_key=True, serialize=False)),
                ('count', models.FloatField()),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('account', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=16)),
                ('phonenumber', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user'),
        ),
        migrations.AddField(
            model_name='dessert',
            name='shops',
            field=models.ManyToManyField(to='myapp.dessert_shop'),
        ),
        migrations.AddField(
            model_name='comment',
            name='dessert_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.dessert', verbose_name='dessert_name'),
        ),
        migrations.AddField(
            model_name='comment',
            name='dessert_shop_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.dessert_shop', verbose_name='shop_name'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user', verbose_name='user_name'),
        ),
    ]
