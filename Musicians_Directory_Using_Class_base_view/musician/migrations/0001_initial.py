# Generated by Django 5.2.3 on 2025-06-26 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('phn_number', models.CharField(max_length=12)),
                ('instrument_type', models.TextField()),
            ],
        ),
    ]
