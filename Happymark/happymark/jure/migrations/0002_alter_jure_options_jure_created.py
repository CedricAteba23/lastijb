# Generated by Django 5.0.4 on 2024-04-08 10:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jure', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jure',
            options={'ordering': ['created']},
        ),
        migrations.AddField(
            model_name='jure',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
