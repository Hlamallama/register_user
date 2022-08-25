from __future__ import annotations
import json
import typing
from django.shortcuts import  render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse, HttpRequest

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, get_user_model

from django.contrib import messages

from .forms import UserCreateForm, UserForm

from .models import User as user_model

UserModel = get_user_model()

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

def read(request: HttpRequest, pk: int) -> typing.Optional[HttpResponse]:
    """
    Read a user login.

    :param request: A HttpRequest object.
    :return: A HttpResponse object.
    """
    form = UserCreationForm()
    users = 0
    if request.user.is_superuser:
        users = UserModel.objects.all()

    return render (request=request, template_name="user/user_view.html",  context={"user_view":form, "all_users": users},)

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
                return redirect("user.user_detail", id=user.id)
            else:
                messages.error(request,"Failed to Authenticate")
        else:
            messages.error(request,"Invalid username or password.")

    form = AuthenticationForm()
    return render(request=request, template_name="user/user_login.html", context={"user_login":form})

def user_detail(request: HttpRequest, id: int) -> HttpResponse:
    """
    View a single user
    """
    if request.user.is_superuser:
        users = UserModel.objects.all()
    context ={}

    context["data"] = UserModel.objects.get(id = 2)
    context["all_users"] = users

    return render(request=request, template_name="user/user_detail.html", context=context)


def update(request: HttpRequest, id: int) -> HttpResponse:
    """
    Update a single user.
    """

    context ={}

    obj = get_object_or_404(UserModel, id = id)

    form = UserForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)

    context["form"] = form

    return render(request=request, template_name="user/user_update.html", context=context)

from django.views.generic.base import TemplateView


class MarkersMapView(TemplateView):
    """Markers map view."""

    template_name = "map.html"
