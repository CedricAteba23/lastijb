from django.shortcuts import render
from sponsor import serializers
from sponsor.models import Sponsor
from rest_framework import generics

# Create your views here.


class SponsorList(generics.ListCreateAPIView):
    queryset= Sponsor.objects.all()
    serializer_class = serializers.SponsorSerializer


class SponsorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= Sponsor.objects.all()
    serializer_class = serializers.SponsorSerializer



# class Jurylist(generics.ListCreateAPIView):
#      queryset= Jury.objects.all()
#      serializer_class = serializers.JurySerializer

# class JuryDetail(generics.RetrieveUpdateDestroyAPIView):
#      queryset= Jury.objects.all()
#      serializer_class = serializers.JurySerializer
