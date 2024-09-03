from django.shortcuts import render
from rest_framework import generics

from critere import serializers
from critere.models import Critere
# Create your views here.


class CritereList(generics.ListCreateAPIView):
        queryset = Critere.objects.all()
        serializer_class = serializers.CritereSerializer


class CritereDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Critere.objects.all()
        serializer_class = serializers.CritereSerializer