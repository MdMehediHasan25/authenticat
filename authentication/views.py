from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login


def home(request):
    return render(request,'authentication/home.html')


def register_view(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = UserCreationForm()

    return render(request, "authentication/register.html", {"form": form})


def login_view(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            user = form.get_user()

            auth_login(request, user)

            return redirect("home")

    else:

        form = AuthenticationForm()

    return render(request, "authentication/login.html", {"form": form})