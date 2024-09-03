from django.db import models


from groupe.models import Groupe
from critere.models import Critere

# Create your models here.
class ActiviteGroupe(models.Model):
    val = models.IntegerField( blank=True, null=True)
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE, blank=True)
    critere =models.ForeignKey(Critere, on_delete=models.CASCADE, blank=True, default=None)
    created = models.DateTimeField(auto_now_add=True)