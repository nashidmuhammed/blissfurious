# Generated by Django 3.1 on 2020-09-08 18:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bliss', '0009_auto_20200908_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
