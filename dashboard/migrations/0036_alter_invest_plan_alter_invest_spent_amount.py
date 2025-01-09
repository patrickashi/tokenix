# Generated by Django 5.0.6 on 2025-01-09 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0035_invest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invest',
            name='plan',
            field=models.CharField(choices=[('standard', 'Standard Plan'), ('expert', 'Expert Plan'), ('ultimate', 'Ultimate Plan'), ('long_term', 'Long Term Investment Stacking')], max_length=20),
        ),
        migrations.AlterField(
            model_name='invest',
            name='spent_amount',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
