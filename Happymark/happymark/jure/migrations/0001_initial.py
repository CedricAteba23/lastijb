# Generated by Django 5.0.4 on 2024-04-08 10:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jury', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, default='', max_length=100)),
                ('prenom', models.CharField(blank=True, default='', max_length=100)),
                ('profession', models.CharField(blank=True, default='', max_length=100)),
                ('role', models.CharField(blank=True, default='', max_length=100)),
                ('jury', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jures', to='jury.jury')),
            ],
        ),
    ]
