# Generated by Django 4.2 on 2023-05-02 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_course_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('PAID', 'Paid'), ('UNPAID', 'Unpaid')], default='PENDING', max_length=20)),
                ('payment_mode', models.CharField(choices=[('Cash', 'Cash'), ('Credit_card', 'Credit Card'), ('Debit_card', 'Debit Card'), ('G-cash', 'Gcash'), ('Paymaya', 'PayMaya')], max_length=20, null=True)),
                ('description', models.CharField(max_length=15, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.student')),
            ],
        ),
    ]