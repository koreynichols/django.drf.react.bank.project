# Generated by Django 3.0.1 on 2019-12-27 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_auto_20191216_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='branch',
            name='location_name',
            field=models.CharField(max_length=100),
        ),
    ]