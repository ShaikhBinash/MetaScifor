# Generated by Django 5.1.6 on 2025-03-06 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='est_date',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
