# Generated by Django 5.1.6 on 2025-03-03 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_ordermodel_is_shipped'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='zip_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
