from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class CustomUser(AbstractUser):
    ORGANISATEUR = 'OR'
    JURY = 'JU'
    JURY_POPULAIRE = 'JP'
    
    ROLE_CHOICES = [
        (ORGANISATEUR, 'Organisateur'),
        (JURY, 'Jury'),
        (JURY_POPULAIRE, 'Jury Populaire'),
    ]
    
    role = models.CharField(max_length=2, choices=ROLE_CHOICES, default=ORGANISATEUR)
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username
    def __str__(self):
        return self.username

