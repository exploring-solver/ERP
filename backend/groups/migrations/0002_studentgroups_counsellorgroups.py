# Generated by Django 4.2.6 on 2023-11-26 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=75)),
                ('group_name', models.ForeignKey(db_column='group_name', null=True, on_delete=django.db.models.deletion.SET_NULL, to='groups.groups')),
                ('student_id', models.OneToOneField(db_column='student_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Student-Groups',
                'db_table': 'student_groups',
            },
        ),
        migrations.CreateModel(
            name='CounsellorGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counsellor_name', models.CharField(max_length=75)),
                ('counsellor_id', models.OneToOneField(db_column='counsellor_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('group_name', models.ForeignKey(db_column='group_name', null=True, on_delete=django.db.models.deletion.SET_NULL, to='groups.groups')),
            ],
            options={
                'verbose_name_plural': 'Counsellor-Groups',
                'db_table': 'counsellor_groups',
            },
        ),
    ]