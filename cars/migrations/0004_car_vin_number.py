# Generated by Django 3.2.4 on 2021-06-28 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20210628_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='vin_number',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
