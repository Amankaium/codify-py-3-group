# Generated by Django 4.2.3 on 2023-08-30 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]