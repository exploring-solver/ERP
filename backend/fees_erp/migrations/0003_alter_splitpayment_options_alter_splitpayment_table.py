# Generated by Django 4.2.6 on 2024-03-05 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fees_erp', '0002_splitpayment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='splitpayment',
            options={'verbose_name_plural': 'Split Payment Approval'},
        ),
        migrations.AlterModelTable(
            name='splitpayment',
            table='split_payment_approval',
        ),
    ]
