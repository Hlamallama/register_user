from django.urls import path
from . import views

app_name = "main"


urlpatterns = [
    path("", views.user_login, name="user_login"),
    path("create", views.create, name="create"),
    path("user_login", views.user_login, name="user_login"),
    path("user_view", views.read, name="user_view")
    ]