# Generated by Django 3.1.5 on 2021-02-02 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_document'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='experience',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='speciality',
            field=models.CharField(max_length=50),
        ),
    ]
