from django.shortcuts import render
from rest_framework import generics
from note import serializers
from note.models import ActiviteGroupe

from note.serializers import ActiviteGroupeSerializer
# Create your views here.


class ActiviteGroupeList(generics.ListCreateAPIView):
    queryset = ActiviteGroupe.objects.all()
    serializer_class = serializers.ActiviteGroupeSerializer

class ActiviteGroupeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= ActiviteGroupe.objects.all()
    serializer_class = serializers.ActiviteGroupeSerializer


