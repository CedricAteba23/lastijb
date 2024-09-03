from rest_framework import serializers
from critere.models import Critere
from groupe.models import Groupe
from note.models import ActiviteGroupe



class ActiviteGroupeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ActiviteGroupe
        fields = ['id', 'val', 'critere', 'groupe', 'created']
    
    def create(self, validated_data):
        groupe_id = self.context['request'].data.get('groupe')
        groupe = Groupe.objects.get(id=groupe_id)
        activite_groupe = ActiviteGroupe.objects.create(groupe=groupe, **validated_data)
        return activite_groupe


# class CritereSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Critere
#         fields = ['id', 'intitule', 'description', 'val']

# class GroupeSerializer(serializers.ModelSerializer):
#     candidats = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

#     class Meta:
#         model = Groupe 
#         fields= ['id', 'nomgroupe', 'description', 'created', 'candidats']