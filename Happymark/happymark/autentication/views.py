from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomUserSerializer, CustomTokenObtainPairSerializer, CreateUserSerializer
from .permissions import IsOrganisateur

User = get_user_model()

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class RegisterOrganisateurView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [permissions.AllowAny]

class CreateJuryView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticated, IsOrganisateur]

    def perform_create(self, serializer):
        serializer.save(role=User.JURY)

class CreateJuryPopulaireView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticated, IsOrganisateur]

    def perform_create(self, serializer):
        serializer.save(role=User.JURY_POPULAIRE)

