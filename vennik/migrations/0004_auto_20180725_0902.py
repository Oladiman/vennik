# Generated by Django 2.0.5 on 2018-07-25 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vennik', '0003_locations'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Locations',
            new_name='Location',
        ),
    ]
