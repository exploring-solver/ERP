# Generated by Django 4.2.6 on 2024-04-21 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placement', '0003_delete_placementofficer_activeplacements_docs_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ActivePlacements',
        ),
        migrations.DeleteModel(
            name='PastPlacements',
        ),
        migrations.AddField(
            model_name='announcement',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='announcement',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]