from django.contrib import admin

from django.contrib.gis.admin import OSMGeoAdmin
from .models import User

@admin.register(User)
class UserAdmin(OSMGeoAdmin):
    list_display = ('username', 'location')
