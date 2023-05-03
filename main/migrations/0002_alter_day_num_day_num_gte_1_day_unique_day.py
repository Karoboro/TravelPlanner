# Generated by Django 4.2 on 2023-05-02 19:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='num',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddConstraint(
            model_name='day',
            constraint=models.CheckConstraint(check=models.Q(('num__gte', 1)), name='num_gte_1'),
        ),
        migrations.AddConstraint(
            model_name='day',
            constraint=models.UniqueConstraint(fields=('trip', 'num'), name='unique_day'),
        ),
    ]
