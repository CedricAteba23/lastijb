# Generated by Django 5.0.4 on 2024-04-13 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('critere', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='critere',
            name='typecritere',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
