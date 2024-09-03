# from rest_framework import generics, status
# from users import serializers

# from survey_authentication.models import User

# from rest_framework import permissions
# from rest_framework.response import Response

# from django_filters.rest_framework import DjangoFilterBackend

# from rest_framework.views import APIView
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from django.contrib.auth import get_user_model

# from users import permissions
# from users.models import User

# UserModel = get_user_model()

# class UserList(generics.ListCreateAPIView):
#     permission_classes = (IsAdminUser, IsAuthenticated )
#     queryset = User.objects.all()
#     serializer_class = serializers.UserSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['email']
    

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (permissions.IsOwnerOrReadOnly, IsAuthenticated )
#     queryset = User.objects.all()
#     serializer_class = serializers.UserSerializer

# from user.models import User
# from authentication.serializers import UserSerializer

from rest_framework import generics, permissions
from .models import User
from .serializers import UserCreateSerializer, UserSerializer, UserSerializer 
from django.contrib.auth import authenticate, login
# from rest_framework.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


# Vue pour l'inscription (organisateur uniquement)
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def inscription(request):
  serializer = UserCreateSerializer(data=request.data)
  if serializer.is_valid():  # Appelez is_valid() avant d'utiliser validated_data
    utilisateur = User.objects.create(**serializer.validated_data)
    utilisateur.set_password(serializer.validated_data['password'])
    utilisateur.save()
    if serializer.data['role'] != 'ORGANISATEUR':
      return Response({'detail': 'Seul l\'organisateur peut s\'inscrire'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vue pour la connexion (tous les rôles sauf organisateur)
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def connexion(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({'detail': 'Veuillez saisir une adresse e-mail et un mot de passe'}, status=status.HTTP_400_BAD_REQUEST)

    utilisateur = authenticate(request, email=email, password=password)
    if utilisateur is None:
        return Response({'detail': 'Identifiants incorrects'}, status=status.HTTP_400_BAD_REQUEST)

    if utilisateur.role == 'ORGANISATEUR':
        return Response({'detail': 'L\'organisateur ne peut pas se connecter via cette API'}, status=status.HTTP_400_BAD_REQUEST)

    login(request, utilisateur)
    return Response({'detail': 'Connexion réussie'}, status=status.HTTP_200_OK)

# Vue pour lister tous les utilisateurs (organisateur uniquement)
class UtilisateurListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role != 'ORGANISATEUR':
            return []
        return User.objects.all()

# Vue pour récupérer les détails d'un utilisateur (tous les rôles)
class UtilisateurDetailAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        utilisateur_id = self.kwargs['pk']
        return User.objects.get(pk=utilisateur_id)

# Vue pour modifier les informations d'un utilisateur (utilisateur concerné uniquement)
class UtilisateurUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        utilisateur_id = self.kwargs['pk']
        return User.objects.get(pk=utilisateur_id)

    def update(self, request, *args, **kwargs):
        utilisateur = self.get_object()
        if utilisateur.id != self.request.user.id:
            return Response({'detail': 'Vous ne pouvez'})


class UtilisateurDeleteAPIView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role != 'ORGANISATEUR':
            return []
        return User.objects.all()

    def destroy(self, request, *args, **kwargs):
        utilisateur = self.get_object()
        if utilisateur.id == self.request.user.id:
            return Response({'detail': 'Vous ne pouvez pas supprimer votre propre compte'}, status=status.HTTP_400_BAD_REQUEST)
        utilisateur.delete()
        return Response({'detail': 'Utilisateur supprimé avec succès'}, status=status.HTTP_204_NO_CONTENT)