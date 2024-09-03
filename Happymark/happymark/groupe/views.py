from django.shortcuts import render
from rest_framework import generics

from groupe import serializers
from groupe.models import Groupe
# Create your views here.


class Groupelist(generics.ListCreateAPIView):
    queryset= Groupe.objects.all()
    serializer_class = serializers.GroupeSerializer

class GroupeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= Groupe.objects.all()
    serializer_class = serializers.GroupeSerializer



