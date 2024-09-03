# etudiant/urls.py
from django.urls import path
from .views import EtudiantListCreate, EtudiantRetrieveUpdateDestroy

urlpatterns = [
    path('etudiants/', EtudiantListCreate.as_view(), name='etudiant-list'),
    path('etudiants/<int:pk>/', EtudiantRetrieveUpdateDestroy.as_view(), name='etudiant-detail'),
]
