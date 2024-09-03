from rest_framework import serializers

from critere.models import Critere
from activite.models import Activite


class CritereSerializer(serializers.ModelSerializer):
    critere = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Critere
        fields = ['id', 'intitule', 'description','activite', 'critere' ]


class ActiviteSerializer(serializers.ModelSerializer):
    # jury = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # candidat= serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # sponsor = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # media = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # critere = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Activite
        fields = ['id', 'nomactivite', 'jury','candidat','criteres','groupe', 'sponsor','media']