# Generated by Django 3.2.7 on 2023-08-12 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0002_auto_20230812_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='abbreviation',
            field=models.CharField(default=None, max_length=2, verbose_name='UF'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='people',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='state', to='registry.state', verbose_name='Estado'),
        ),
    ]
