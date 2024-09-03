from django.db import models

from jury.models import Jury

# Create your models here.




class Jure(models.Model):
    nom=models.CharField(max_length=100, blank=True, default='')
    prenom= models.CharField(max_length=100, blank=True, default='')
    profession=models.CharField(max_length=100, blank=True, default='')
    role=models.CharField(max_length=100, blank=True, default='')
    jury=  models.ForeignKey(Jury, related_name='jures', on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['created']