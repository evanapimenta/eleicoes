# Generated by Django 3.2.7 on 2023-08-12 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0006_auto_20230812_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='address',
        ),
    ]