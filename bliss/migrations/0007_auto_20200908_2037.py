# Generated by Django 3.1 on 2020-09-08 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bliss', '0006_auto_20200828_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='replay',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
