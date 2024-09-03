from rest_framework import serializers
from django.conf import settings

from groupe.models import Groupe
from candidat.models import Candidat


class CandidatSerializer(serializers.ModelSerializer):
     class Meta:
         model= Candidat
         fields =['nom', 'prenom', 'groupe', 'created']
         


class GroupeSerializer(serializers.ModelSerializer):
    candidats = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Groupe 
        fields= ['id', 'nomgroupe', 'description', 'created']