# Generated by Django 4.2.6 on 2023-10-23 06:36

from django.db import migrations, models
import student.utils


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_studentdetails_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='aadhar',
            field=models.FileField(blank=True, null=True, upload_to=student.utils.aadhar_rename),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='marksheet_10th',
            field=models.FileField(blank=True, null=True, upload_to=student.utils.marksheet_10th_rename),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='marksheet_12th',
            field=models.FileField(blank=True, null=True, upload_to=student.utils.marksheet_12th_rename),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='pancard',
            field=models.FileField(blank=True, null=True, upload_to=student.utils.pancard_rename),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='passport_photograph',
            field=models.ImageField(blank=True, null=True, upload_to=student.utils.passport_photograph_rename),
        ),
    ]