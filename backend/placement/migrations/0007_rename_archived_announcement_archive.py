# <<<<<<< HEAD
# Generated by Django 4.2.6 on 2024-04-22 18:29
# =======
# Generated by Django 4.2.6 on 2024-04-22 19:29
# >>>>>>> e1a95461e4b99065c19c192056fad219777692d5

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('placement', '0006_announcement_archived'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcement',
            old_name='archived',
            new_name='archive',
        ),
    ]
