# Generated by Django 4.2 on 2023-05-01 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_contactbuy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('bank_account', models.IntegerField()),
                ('rent_amount', models.IntegerField()),
            ],
            options={
                'db_table': 'amount',
            },
        ),
    ]
