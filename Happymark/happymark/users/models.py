# from operator import truediv
# from django.db import models
# from django.contrib.auth.base_user import BaseUserManager
# from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.models import AbstractUser

# Create your models here.
# class UserManager(BaseUserManager):
    
#     def create_user(self, email, username, password, **extra_fields):
#         if not email:
#             raise ValueError(_("You should provide an email address"))
        
#         if not username:
#             raise ValueError(_("You should provide a Username"))
        
#         if not password:
#             raise ValueError(_("You should provide a password"))
        
#         email = self.normalize_email(email)
        
#         user = self.model(username = username, email =email, **extra_fields)
#         user.set_password(password)
#         user.save()
        
#         return user
    
#     def create_superuser(self, email, username, password, **extra_fields):
#         extra_fields.setdefault("is_superuser", True)
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_active", True)
        
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError(_("Super User must have is_superuser = True"))
        
#         if extra_fields.get("is_staff") is not True:
#             raise ValueError(_("Super User must have is_staff = True"))
        
#         if extra_fields.get("is_active") is not True:
#             raise ValueError(_("Super User must have is_active = True"))
        
        
#         return self.create_user(email, username, password, **extra_fields)
    
# class User(AbstractUser):
#     username = models.CharField(max_length=100, null=True, blank=False, unique=True)
#     email = models.EmailField(max_length=150, null=True, blank=False, unique=True)
    
#     first_name = models.CharField(max_length=255, null=True, blank=True)
#     last_name = models.CharField(max_length=255, null=True, blank=True)
    
#     address = models.CharField(max_length=255, null=True, blank=True)
#     date_joined = models.DateTimeField(blank=True, null=True, auto_now_add=True)
#     last_update = models.DateTimeField(blank=True, null=True, auto_now=True)
    # is_enqueteur = models.BooleanField(null=True, blank=True)
    
    # REQUIRED_FIELDS = ['email']
    # USERNAME_FIELD = "username"

    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     related_name='custom_user_set',
    #     blank=True,
    #     verbose_name='groups',
    #     help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    # )

    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     related_name='custom_user_set',
    #     blank=True,
    #     verbose_name='user permissions',
    #     help_text='Specific permissions for this user.',
    # )
    
    # objects = UserManager()
    
    # class Meta:
    #     verbose_name = "User"
    #     verbose_name_plural = "Users"
    #     ordering = ["-date_joined"]
        
    # def __str__(self):
    #     return self.username

# 


from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Rôles des utilisateurs
ROLES = [
    ('ORGANISATEUR', 'Organisateur'),
    ('JURY', 'Jury'),
    ('MEDIA', 'Médias'),
    ('JURY_POPULAIRE', 'Jury Populaire'),
]


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Les utilisateurs doivent avoir une adresse e-mail')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Les superutilisateurs doivent être des membres du personnel')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Les superutilisateurs doivent avoir le statut de superutilisateur')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    pass
    # USERNAME_FIELD = 'email'
    # email = models.EmailField(unique=True, max_length=255)
    # nom = models.CharField(max_length=255)
    # prenom = models.CharField(max_length=255)
    # role = models.CharField(max_length=255, choices=ROLES, default='JURY_POPULAIRE')
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)

    # REQUIRED_FIELDS = ['email', 'nom', 'prenom', 'role']
    # USERNAME_FIELD = 'email'

    # objects = UserManager()

    # def __str__(self):
    #     return f"{self.nom} {self.prenom}"

    # def has_perm(self, perm, obj=None):
    #     return self.is_staff

    # def has_module_perms(self, app_label):
    #     return self.is_staff
