from django.contrib.auth.models import AbstractUser

from django.db.models import CharField


class User(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )

    role = CharField(max_length=10, choices=ROLES, default='user')

    