# Generated by Django 5.1.7 on 2025-03-15 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=15)),
                ('start_end_time', models.CharField(choices=[('08:00-16:00', '08:00 AM - 04:00 PM'), ('09:00-17:00', '09:00 AM - 05:00 PM'), ('10:00-18:00', '10:00 AM - 06:00 PM'), ('24/7', 'Open 24/7')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Specialities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
