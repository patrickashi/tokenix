# Generated by Django 5.1.4 on 2025-01-29 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0038_invest_crypto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Withdrawal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=8, max_digits=20, null=True)),
                ('crypto', models.CharField(blank=True, choices=[('BTC', 'Bitcoin'), ('USDT', 'Usdt'), ('ETH', 'Ethereum')], max_length=5, null=True)),
                ('wallet_address', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='invest',
            name='crypto',
            field=models.CharField(blank=True, choices=[('BTC', 'Bitcoin (BTC)'), ('ETH', 'Ethereum (ETH)'), ('USDT', 'Usdt (USDT)')], max_length=10, null=True),
        ),
    ]
