# Generated by Django 5.0.4 on 2024-08-19 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activite', '0008_activite_sp_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activite',
            name='sp_id',
        ),
        migrations.AddField(
            model_name='activite',
            name='sp',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
