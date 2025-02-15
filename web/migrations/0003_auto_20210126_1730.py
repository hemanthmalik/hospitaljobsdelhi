# Generated by Django 3.1.5 on 2021-01-26 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_jobseeker_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseeker',
            name='current_company',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='email',
            field=models.EmailField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='expected_salary',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='experience',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='gender',
            field=models.CharField(choices=[('Male', 'male'), ('Female', 'female'), ('Other', 'other')], default=None, max_length=6),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='phone',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='qualification',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='speciality',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='first_name',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='last_name',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
