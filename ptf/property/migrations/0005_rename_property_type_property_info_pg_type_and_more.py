# Generated by Django 4.2 on 2023-05-01 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_property_info_bhk'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property_info',
            old_name='property_type',
            new_name='PG_type',
        ),
        migrations.RenameField(
            model_name='property_info',
            old_name='builders_name',
            new_name='owners_name',
        ),
        migrations.RenameField(
            model_name='property_info',
            old_name='price',
            new_name='rent',
        ),
        migrations.RemoveField(
            model_name='property_info',
            name='rera',
        ),
    ]