# Generated by Django 5.0.4 on 2024-04-16 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='forecastData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fcstDate', models.CharField(max_length=8)),
                ('fcstTime', models.CharField(max_length=2)),
                ('fcstValue', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=10)),
            ],
        ),
    ]
