# Generated by Django 4.1.4 on 2023-02-05 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chq_app', '0005_master_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='date',
            field=models.DateField(),
        ),
    ]