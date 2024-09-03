from django.db import models

# Create your models here.


class Media(models.Model):
    nomMedia = models.CharField(max_length=100, blank=True, default='')
    # logo = models.ImageField(blank=True, null=True, default='', upload_to=upload_path)