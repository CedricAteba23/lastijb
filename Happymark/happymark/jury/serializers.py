from rest_framework import serializers
from django.conf import settings

from jury.models import Jury


class JurySerializer(serializers.ModelSerializer):
    jure = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Jury
        fields= ['id', 'nomjury', 'description', 'created', 'jure']




