# Generated by Django 5.1.6 on 2025-03-06 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='landlord',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='landlord',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
