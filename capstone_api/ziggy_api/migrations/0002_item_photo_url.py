# Generated by Django 4.2 on 2023-04-27 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ziggy_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='photo_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
