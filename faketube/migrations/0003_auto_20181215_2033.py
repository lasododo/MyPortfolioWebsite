# Generated by Django 2.0.7 on 2018-12-15 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faketube', '0002_auto_20181209_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoupload',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
