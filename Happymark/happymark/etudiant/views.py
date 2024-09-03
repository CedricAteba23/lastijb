from django.shortcuts import render

# Create your views here.
# etudiant/views.py
from rest_framework import generics
from .models import Etudiant
from .serializers import EtudiantSerializer

class EtudiantListCreate(generics.ListCreateAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer

class EtudiantRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
