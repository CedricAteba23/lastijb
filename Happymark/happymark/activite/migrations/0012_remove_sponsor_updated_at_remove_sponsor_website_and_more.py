# Generated by Django 5.0.4 on 2024-09-03 10:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activite', '0011_sponsor_remove_activite_sponsor_id_activite_sponsor'),
        ('groupe', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsor',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='website',
        ),
        migrations.AlterField(
            model_name='activite',
            name='groupe',
            field=models.ManyToManyField(blank=True, default='', related_name='activite', to='groupe.groupe'),
        ),
        migrations.AlterField(
            model_name='activite',
            name='organisateur',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activites', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
