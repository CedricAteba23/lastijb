from rest_framework import serializers
from django.conf import settings
from media.models import Media


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'nomMedia']