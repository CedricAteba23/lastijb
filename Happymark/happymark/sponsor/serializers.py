from rest_framework import serializers
from django.conf import settings
from sponsor.models import Sponsor


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ['id', 'nomsponsor', 'logo']