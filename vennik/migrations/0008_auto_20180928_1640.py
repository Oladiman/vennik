# Generated by Django 2.0.5 on 2018-09-28 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vennik', '0007_auto_20180924_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='name',
        ),
        migrations.AlterField(
            model_name='apartment',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='good',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
