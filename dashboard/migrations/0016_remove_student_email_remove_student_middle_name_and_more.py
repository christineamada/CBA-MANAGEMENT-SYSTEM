# Generated by Django 4.2 on 2023-05-23 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_rename_clearance_studentclearance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='middle_name',
        ),
        migrations.AddField(
            model_name='student',
            name='middle_initial',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
