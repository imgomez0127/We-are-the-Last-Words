# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-20 01:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('text', models.TextField()),
                ('Post_Image', models.ImageField(blank=True, upload_to='post_imgs/')),
                ('credits', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reccommended_Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('Book_Image', models.ImageField(blank=True, upload_to='post_imgs/')),
                ('Buy_Link', models.CharField(blank=True, max_length=2083)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='Book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blogsite.Reccommended_Book'),
        ),
    ]
