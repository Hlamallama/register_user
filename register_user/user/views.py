from __future__ import annotations
import typing
from django.shortcuts import  render, redirect
from django.http import HttpResponse, HttpRequest

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, get_user_model

from django.contrib import messages

from .forms import UserCreateForm

User = get_user_model()

def user_login(request: HttpRequest) -> HttpResponse:
    """
    Auntheticates a user login.

    :param request: A HttpRequest object.
    :return: A HttpResponse object.
    """

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("main:user_view")
            else:
                messages.error(request,"Failed to Authenticate")
        else:
            messages.error(request,"Invalid username or password.")

    form = AuthenticationForm()
    return render(request=request, template_name="user/user_login.html", context={"user_login":form})

def create(request: HttpRequest) -> HttpResponse:
    """
    Auntheticates a user login.

    :param request: A HttpRequest object.
    :return: A HttpResponse object.
    """

    if request.method == "POST":
        form = UserCreateForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main:user_view")

        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = UserCreateForm()
    return render (request=request, template_name="user/user_register.html", context={"user_register":form})

def read(request: HttpRequest) -> typing.Optional[HttpResponse]:
    """
    Auntheticates a user login.

    :param request: A HttpRequest object.
    :return: A HttpResponse object.
    """

    form = UserCreationForm()
    users = None
    if request.user.is_superuser:
        users = User.objects.all()
        return render (request=request, template_name="user/user_view.html",  context={"user_view":form, "all_users": users},)
