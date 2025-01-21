# Generated by Django 5.1.4 on 2025-01-21 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0037_alter_invest_profit_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='invest',
            name='crypto',
            field=models.CharField(blank=True, choices=[('BTC', 'Bitcoin (BTC)'), ('ETH', 'Ethereum (ETH)'), ('USDT', 'Tether (USDT)')], max_length=10, null=True),
        ),
    ]
