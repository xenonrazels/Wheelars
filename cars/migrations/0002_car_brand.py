# Generated by Django 3.2.4 on 2021-07-01 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='brand',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]