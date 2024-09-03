from django.db import models

# Create your models here.

def upload_path(instance, filename):
    return '/'.join(['logos', str(instance.nomsponsor), filename])

class Sponsor(models.Model):
    nomsponsor = models.CharField(max_length=100, blank=True, default='')
    logo = models.ImageField(blank=True, null=True, default='', upload_to=upload_path)
