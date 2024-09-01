from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, update_session_auth_hash
from accounts.forms import ProfileForm, CustomPasswordChangeForm


from .forms import CustomUserCreationForm, ProfileForm


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


@login_required
def edit_profile(request):
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)

        if "profile_submit" in request.POST:
            if profile_form.is_valid():
                profile_form.save()
                return redirect("main:main")
        elif "password_submit" in request.POST:
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # 비밀번호 변경 후 세션 유지
                return redirect("main:main")
    else:
        profile_form = ProfileForm(instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user)

    context = {
        "profile_form": profile_form,
        "password_form": password_form,
    }

    return render(request, "accounts/profile.html", context)
