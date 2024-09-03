from rest_framework import serializers
from activite.models import Activite
from groupe.models import Groupe
from candidat.models import Candidat
from critere.models import Critere
from sponsor.models import Sponsor
from media.models import Media
from jury.models import Jury


class CritereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Critere
        fields = ['id', 'intitule', 'description']
        
class CandidatSerializer(serializers.ModelSerializer):
     class Meta:
         model= Candidat
         fields =['nom', 'prenom', 'groupe', 'created']

class GroupeSerializer(serializers.ModelSerializer):
    candidats = CandidatSerializer(many=True, read_only=True)

    class Meta:
        model = Groupe 
        fields= ['id', 'nomgroupe', 'description','candidats', 'created']
    
class ActiviteSerializer(serializers.ModelSerializer):
    criteres = CritereSerializer(read_only=True, many=True)
    groupe =  GroupeSerializer(read_only=True, many=True)
   
    # criteres = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # jury = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # candidat= serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # sponsor = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # media = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # critere = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Activite
        fields = ['id', 'nomactivite','criteres', 'groupe', 'sponsor','organisateur']




class CandidatSerializer(serializers.ModelSerializer):
     class Meta:
         model= Candidat
         fields =['nom', 'prenom', 'groupe', 'created']
 
         



class JurySerializer(serializers.ModelSerializer):
    jure = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Jury
        fields= ['id', 'nomjury', 'description', 'created', 'jure']


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'nomMedia']

# class SponsorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sponsor
#         fields = ['id', 'nomsponsor', 'logo']


