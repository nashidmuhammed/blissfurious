# Generated by Django 3.1 on 2020-08-25 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bliss', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='art_id',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
