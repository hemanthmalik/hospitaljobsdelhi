# Generated by Django 3.1.5 on 2021-01-26 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20210126_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='current_organization',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='expected_salary',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='experience',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=6),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='qualification',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='resume',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='speciality',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
