# Generated by Django 4.2 on 2023-05-09 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_alter_transaction_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='link2',
            field=models.URLField(max_length=150, null=True),
        ),
    ]
