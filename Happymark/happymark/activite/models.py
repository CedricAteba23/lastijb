from django.db import models
from autentication.models import CustomUser
from candidat.models import Candidat
from groupe.models import Groupe
from media.models import Media
# from sponsor.models import Sponsor
from jury.models import Jury
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

# Create your models here.
class Sponsor(models.Model):
    # Les mêmes champs que dans le microservice
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name 

class Activite(models.Model):
    nomactivite= models.CharField(max_length=100, blank=True, default='')
    # jury = models.ForeignKey(Jury, related_name='jury', on_delete=models.CASCADE)
    # candidat= models.ForeignKey(Candidat, related_name='candidat', on_delete=models.CASCADE, blank=True)
    groupe = models.ManyToManyField(Groupe, related_name='activite',  blank=True, default='')
    sponsor = models.ForeignKey(Sponsor, on_delete=models.SET_NULL, null=True, blank=True, default='')
    # media = models.ForeignKey(Media, related_name='media', on_delete=models.CASCADE)
    organisateur = models.ForeignKey(CustomUser, related_name='activites', null=True, blank=True, on_delete=models.CASCADE, default='')

