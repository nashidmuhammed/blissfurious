# Generated by Django 3.1 on 2020-09-08 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bliss', '0007_auto_20200908_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
