# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-28 21:40
from __future__ import unicode_literals

import ListWeb.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ListWeb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to=ListWeb.models.upload_image_path),
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=ListWeb.models.upload_image_path),
        ),
    ]
