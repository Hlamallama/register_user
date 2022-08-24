from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """The User model"""

    home_address = models.TextField(max_length=250, blank=True)
    phone_number = models.TextField(max_length=30, blank=True)
    location = models.TextField(blank=True)
    is_superuser = models.BooleanField(default=False)
