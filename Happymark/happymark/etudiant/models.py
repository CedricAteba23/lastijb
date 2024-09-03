# from django.db import models

# Create your models here.
# etudiant/views.py
# etudiant/models.py
from django.db import models

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.nom


