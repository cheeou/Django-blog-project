from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User


class CustomUserCreationForm(UserCreationForm):
    nickname = forms.CharField(
        max_length=30, required=True, help_text="Required. 30 characters or fewer."
    )
    profile_image = forms.ImageField(required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = (
            "username",
            "nickname",
            "profile_image",
            "bio",
            "password1",
            "password2",
        )

    def clean_nickname(self):
        nickname = self.cleaned_data.get("nickname")
        if User.objects.filter(nickname=nickname).exists():
            raise forms.ValidationError("A user with that nickname already exists.")
        return nickname

    def save(self, commit=True):
        user = super().save(commit=False)
        user.nickname = self.cleaned_data["nickname"]
        if commit:
            user.save()
        return user
