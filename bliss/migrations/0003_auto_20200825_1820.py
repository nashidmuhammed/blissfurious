# Generated by Django 3.1 on 2020-08-25 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bliss', '0002_auto_20200825_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='art_id',
            field=models.CharField(max_length=100),
        ),
    ]
