from django.shortcuts import render
from rest_framework import generics
from activite.models import Activite, Sponsor
from activite import serializers


# Create your views here.


class ActiviteList(generics.ListCreateAPIView):
    queryset = Activite.objects.all()
    serializer_class = serializers.ActiviteSerializer

    def get_queryset(self):
        return Activite.objects.filter(organisateur=self.request.user)

    def perform_create(self, serializer):
        serializer.save(organisateur=self.request.user)

class ActiviteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activite.objects.all()
    serializer_class = serializers.ActiviteSerializer

    def get_queryset(self):
        return Activite.objects.filter(organisateur=self.request.user)
    

