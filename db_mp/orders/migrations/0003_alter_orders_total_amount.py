# Generated by Django 5.1.3 on 2025-01-10 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_orders_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
