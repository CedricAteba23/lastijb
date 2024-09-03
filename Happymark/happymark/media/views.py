from django.shortcuts import render
from rest_framework import generics
from media import serializers
from media.models import Media
# Create your views here.

class MediaList(generics.ListCreateAPIView):
    queryset = Media.objects.all()
    serializer_class = serializers.MediaSerializer


class MediaDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Media.objects.all()
        serializer_class = serializers.MediaSerializer