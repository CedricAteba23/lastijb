from django.shortcuts import render
from rest_framework import generics
from jury import serializers
from jury.models import Jury
# Create your views here.


class Jurylist(generics.ListCreateAPIView):
     queryset= Jury.objects.all()
     serializer_class = serializers.JurySerializer

class JuryDetail(generics.RetrieveUpdateDestroyAPIView):
     queryset= Jury.objects.all()
     serializer_class = serializers.JurySerializer


