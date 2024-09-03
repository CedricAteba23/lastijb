from django.db import models

from activite.models import Activite

class Critere(models.Model):
    intitule = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    typecritere= models.CharField(max_length=100, blank=True, default='')
    activite = models.ForeignKey(Activite, related_name='criteres', on_delete=models.CASCADE ,default=None)  