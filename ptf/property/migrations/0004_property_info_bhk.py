# Generated by Django 4.1.7 on 2023-04-26 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_city_property_type_property_info_garden_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='property_info',
            name='BHK',
            field=models.IntegerField(default=True),
        ),
    ]
