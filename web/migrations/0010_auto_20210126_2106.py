# Generated by Django 3.1.5 on 2021-01-26 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_jobposting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobposting',
            name='salary_offering',
            field=models.CharField(blank=True, default=0, max_length=20),
            preserve_default=False,
        ),
    ]
