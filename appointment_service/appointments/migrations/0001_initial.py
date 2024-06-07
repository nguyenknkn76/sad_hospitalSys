# Generated by Django 3.2.25 on 2024-06-03 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.IntegerField()),
                ('doctor_id', models.IntegerField()),
                ('appointment_date', models.DateField()),
                ('appointment_time', models.TimeField()),
                ('appointment_type', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], max_length=20)),
            ],
        ),
    ]