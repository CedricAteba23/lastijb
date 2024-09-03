from django.db import models

# Create your models here.

class Groupe(models.Model):
    nomgroupe=models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['created']