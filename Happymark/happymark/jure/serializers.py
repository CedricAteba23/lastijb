from rest_framework import serializers
from django.conf import settings

from jure.models import Jure
from jury.models import Jury


class JureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jure
        fields =['nom', 'prenom', 'profession', 'role','jury',  'created']


class JurySerializer(serializers.ModelSerializer):
    jure = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Jury
        fields= ['id', 'nomjury', 'description', 'created', 'jure']


