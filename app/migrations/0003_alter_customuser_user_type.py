# Generated by Django 5.0.7 on 2024-07-17 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_appointment_appointmentdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('0', 'SUPERADMIN'), ('1', 'HOC'), ('2', 'DOCTOR'), ('3', 'PATIENT')], default='1', max_length=10),
        ),
    ]
