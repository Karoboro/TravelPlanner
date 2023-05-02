# Generated by Django 4.2 on 2023-05-01 21:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('Accommodation', 'Accommodation'), ('Transportation', 'Transportation'), ('Entertainment', 'Entertainment'), ('Food', 'Food')], max_length=200)),
                ('time', models.TimeField(verbose_name='Start Time')),
                ('location', models.CharField(max_length=200)),
                ('cost', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('description', models.CharField(max_length=200)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.day')),
            ],
        ),
        migrations.AddField(
            model_name='day',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.trip'),
        ),
    ]