from django.shortcuts import render
from rest_framework import generics
from candidat.models import Candidat
from candidat import serializers


# Create your views here.



class Candidatlist(generics.ListCreateAPIView):
    queryset = Candidat.objects.all()
    serializer_class = serializers.CandidatSerializer


class CandidatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidat.objects.all()
    serializer_class = serializers.CandidatSerializer

    
# class Groupelist(generics.ListCreateAPIView):
#     queryset= Groupe.objects.all()
#     serializer_class = serializers.GroupeSerializer

# class GroupeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset= Groupe.objects.all()
#     serializer_class = serializers.GroupeSerializer
