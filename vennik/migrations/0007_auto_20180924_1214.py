# Generated by Django 2.0.5 on 2018-09-24 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vennik', '0006_goods'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Apartments',
            new_name='Apartment',
        ),
        migrations.RenameModel(
            old_name='Goods',
            new_name='Good',
        ),
    ]