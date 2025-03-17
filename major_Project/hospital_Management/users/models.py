from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)
    has_hospital = models.BooleanField(default=False)
    
    is_patient = models.BooleanField(default=False)
    has_profile = models.BooleanField(default=False)
    

    groups = models.ManyToManyField(Group, related_name="custom_user_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions_set", blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

