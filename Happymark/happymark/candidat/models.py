from django.db import models

from groupe.models import Groupe

# Create your models here.


class Candidat(models.Model):
    nom = models.CharField(max_length=100, blank=True, default='')
    prenom=models.CharField(max_length=100, blank=True, default='')
    groupe = models.ForeignKey(Groupe, related_name='candidats', on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['created']