from django.db import models

# Create your models here.
from django.db import models

class SponsorProxy(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False  # Django ne gère pas ce modèle en base de données
        verbose_name = 'Sponsor'
        verbose_name_plural = 'Sponsors'

    def __str__(self):
        return self.name