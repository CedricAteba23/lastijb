# Generated by Django 5.0.4 on 2024-04-13 13:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activite', '0003_alter_activite_candidat'),
        ('critere', '0002_critere_typecritere'),
    ]

    operations = [
        migrations.AddField(
            model_name='critere',
            name='activite',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='criteres', to='activite.activite'),
        ),
    ]
