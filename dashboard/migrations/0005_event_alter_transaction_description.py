# Generated by Django 4.2 on 2023-05-02 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.CharField(max_length=50, null=True)),
                ('event_name', models.CharField(max_length=50, null=True)),
                ('date', models.DateField(null=True)),
                ('description', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='transaction',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
