# from django.contrib import admin

# Register your models here.
# from django.contrib import admin

# from sponsor.models import Sponsor

# # Register your models here.
# admin.site.register(Sponsor)
from django.contrib import admin
from .models import SponsorProxy
import requests
from django.conf import settings

@admin.register(SponsorProxy)
class SponsorProxyAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    readonly_fields = ('id', 'created_at', 'updated_at')

    def get_queryset(self, request):
        # Récupérer les données depuis le microservice
        response = requests.get(f"{settings.SPONSOR_SERVICE_URL}/sponsors/")
        if response.status_code == 200:
            sponsors_data = response.json()
            return [SponsorProxy(**sponsor) for sponsor in sponsors_data]
        return []

    def has_add_permission(self, request):
        return False  # Désactive l'ajout via l'admin

    def has_delete_permission(self, request, obj=None):
        return False  # Désactive la suppression via l'admin

    def save_model(self, request, obj, form, change):
        # Envoyer les modifications au microservice
        data = {
            'name': obj.name,
            'description': obj.description,
            'website': obj.website,
        }
        if change:  # Si c'est une modification
            response = requests.put(f"{settings.SPONSOR_SERVICE_URL}/sponsors/{obj.id}/", json=data)
        else:  # Si c'est une création
            response = requests.post(f"{settings.SPONSOR_SERVICE_URL}/sponsors/", json=data)
        
        if response.status_code not in [200, 201]:
            raise Exception("Erreur lors de la sauvegarde du sponsor dans le microservice")

    def delete_model(self, request, obj):
        # Envoyer la demande de suppression au microservice
        response = requests.delete(f"{settings.SPONSOR_SERVICE_URL}/sponsors/{obj.id}/")
        if response.status_code != 204:
            raise Exception("Erreur lors de la suppression du sponsor dans le microservice")
