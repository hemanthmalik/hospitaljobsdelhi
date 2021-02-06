# Generated by Django 3.1.5 on 2021-01-26 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20210126_1730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobseeker',
            old_name='current_company',
            new_name='current_organization',
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='gender',
            field=models.CharField(choices=[('', 'Gender'), ('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default=None, max_length=6),
        ),
    ]
