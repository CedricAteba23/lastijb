from django.shortcuts import render
from rest_framework import generics
from jure import serializers
from jure.models import Jure
# Create your views here.

class JureList(generics.ListCreateAPIView):
    queryset = Jure.objects.all()
    serializer_class = serializers.JureSerializer

class JureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jure.objects.all()
    serializer_class = serializers.JureSerializer


