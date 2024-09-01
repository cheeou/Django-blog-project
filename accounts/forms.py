from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
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


User = get_user_model()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["nickname", "profile_image", "bio"]

        widgets = {
            "nickname": forms.TextInput(attrs={"class": "form-control"}),
            "profile_image": forms.FileInput(attrs={"class": "form-control-file"}),
            "bio": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False

    def clean_nickname(self):
        nickname = self.cleaned_data.get("nickname")
        if (
            nickname
            and User.objects.filter(nickname=nickname)
            .exclude(pk=self.instance.pk)
            .exists()
        ):
            raise forms.ValidationError("This nickname is already in use.")
        return nickname


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False
