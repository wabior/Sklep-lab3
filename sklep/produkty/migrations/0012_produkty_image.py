# Generated by Django 2.2 on 2019-04-27 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkty', '0011_auto_20190423_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='produkty',
            name='image',
            field=models.FileField(blank=True, upload_to='image'),
        ),
    ]
