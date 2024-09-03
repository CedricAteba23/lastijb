from rest_framework import serializers
# from survey_authentication.models import User
from django.contrib.auth import get_user_model

UserModel = get_user_model()


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         # exclude = ('password', )
        #    enquetes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#         fields = ['id', 'username', 'email', 'first_name', 'last_name', 'address', 'enquetes']

#     def createUser(self, validated_data):
#         user = UserModel(**validated_data)
#         user.set_password(validated_data['password'])
#         user.save()
#         return user

# class UserSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(max_length=100, allow_blank=False)
#     email = serializers.EmailField(max_length=100, allow_blank=False)
#     password = serializers.CharField(max_length=50, allow_blank=False)
#     enquetes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     formulaires = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

#     class Meta:
#         model = UserModel
#         fields = ["id", "username", "email", "password"]

#     def create(self, validated_data):
#         user = UserModel(**validated_data)
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
    
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'nom', 'prenom', 'role']

class UserCreateSerializer(serializers.ModelSerializer):
  
  class Meta:
        model = User
        fields = ['email', 'nom', 'prenom', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # Masquer le mot de passe

def create(self, validated_data):
        password = validated_data.pop('password')
        utilisateur = User.objects.create(**validated_data)
        utilisateur.set_password(password)
        utilisateur.save()
        return utilisateur