# Generated by Django 5.1.6 on 2025-03-07 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_industry_state_job_job_type_job_industry_job_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='state',
        ),
        migrations.DeleteModel(
            name='State',
        ),
    ]
