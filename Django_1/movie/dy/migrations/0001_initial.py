# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 04:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DyModels',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('link', models.CharField(max_length=100)),
            ],
        ),
    ]
