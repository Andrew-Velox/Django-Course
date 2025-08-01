# Generated by Django 5.2.3 on 2025-06-26 15:14

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=40)),
                ('relase_date', models.DateField(default=datetime.date.today)),
                ('raing', models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five')], max_length=10)),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musician.musician')),
            ],
        ),
    ]
