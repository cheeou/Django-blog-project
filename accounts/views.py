from django.contrib.auth import logout, login
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm


def logout_view(request):
    logout(request)
    return redirect("/main/")


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("main:main"))
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})
