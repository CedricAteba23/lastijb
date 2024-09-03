# Dans un nouveau fichier, par exemple 'services/sponsor_service.py'
import requests
from django.conf import settings
from activite.models import SponsorReference  # Ajustez le chemin d'importation selon votre structure

def get_or_create_sponsor_reference(sponsor_data):
    sponsor_ref, created = SponsorReference.objects.get_or_create(
        external_id=sponsor_data['id'],
        defaults={'name': sponsor_data['name']}
    )
    if not created and sponsor_ref.name != sponsor_data['name']:
        sponsor_ref.name = sponsor_data['name']
        sponsor_ref.save()
    return sponsor_ref

def get_sponsor_details(sponsor_id):
    response = requests.get(f"{settings.SPONSOR_SERVICE_URL}/sponsors/{sponsor_id}/")
    if response.status_code == 200:
        sponsor_data = response.json()
        return get_or_create_sponsor_reference(sponsor_data)
    return None