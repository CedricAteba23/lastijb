# Generated by Django 5.0.4 on 2024-04-08 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jury',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomjury', models.CharField(blank=True, default='', max_length=100)),
                ('description', models.CharField(blank=True, default='', max_length=100)),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
