# Generated by Django 5.0 on 2023-12-08 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0002_rename_units_unit'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Unit',
            new_name='Units',
        ),
    ]
