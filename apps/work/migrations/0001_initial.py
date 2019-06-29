# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-17 07:49
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('summary', models.TextField()),
                ('video', models.CharField(blank=True, max_length=5000)),
                ('description', models.TextField()),
                ('tech', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1000), size=None)),
                ('github', models.CharField(blank=True, max_length=5000)),
                ('deploy', models.CharField(blank=True, max_length=5000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
