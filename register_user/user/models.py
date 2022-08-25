from email.policy import default
from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """The User model"""

    home_address = models.TextField(max_length=250, blank=True)
    phone_number = models.CharField(max_length=30, blank=True)
    location = gis_models.PointField(blank=True)
    is_superuser = models.BooleanField(default=False)
