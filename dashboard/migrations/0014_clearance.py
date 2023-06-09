# Generated by Django 4.2 on 2023-05-16 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_alter_schoolyear_semester'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clearance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('CLEARED', 'Cleared')], default='PENDING', max_length=50)),
                ('schoolyear', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.schoolyear')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.student')),
            ],
        ),
    ]
