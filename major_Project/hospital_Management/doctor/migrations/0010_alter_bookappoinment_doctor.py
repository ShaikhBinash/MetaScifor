# Generated by Django 5.1.7 on 2025-03-16 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0009_doctor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookappoinment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='doctor.doctor'),
        ),
    ]
