# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State_ID', models.IntegerField()),
                ('Comment_User_name', models.CharField(max_length=32)),
                ('content', models.CharField(max_length=255)),
                ('IsMap', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='GMap',
            fields=[
                ('Map_ID', models.BigIntegerField(primary_key=True, serialize=False)),
                ('Col', models.IntegerField()),
                ('Row', models.IntegerField()),
                ('Content', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_name', models.CharField(max_length=32)),
                ('Password', models.CharField(max_length=32)),
                ('Map_ID', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_name', models.CharField(max_length=32)),
                ('Map_ID', models.BigIntegerField()),
                ('Like', models.IntegerField(default=0)),
                ('Commentno', models.IntegerField(default=0)),
                ('Read', models.IntegerField(default=0)),
                ('Timestamp', models.DateTimeField(auto_now=True)),
                ('Feeling', models.CharField(max_length=32, null=True)),
            ],
        ),
    ]
