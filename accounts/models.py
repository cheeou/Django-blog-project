from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    nickname = models.CharField("닉네임", max_length=30, unique=True)
    profile_image = models.ImageField(
        "프로필 이미지", upload_to="accounts/proile", blank=True
    )
    bio = models.TextField("소개글", blank=True)
