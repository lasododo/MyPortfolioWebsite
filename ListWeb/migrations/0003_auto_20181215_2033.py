# Generated by Django 2.0.7 on 2018-12-15 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ListWeb', '0002_auto_20180628_2340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]