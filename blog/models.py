from django.db import models
from django.utils import timezone
from django.conf import settings
from utils.validators import validate_post_title, validate_post_content


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="작성자",
        null=True,
        blank=True,
    )
    postTitle = models.CharField(
        "포스트 제목",
        max_length=50,
        validators=[validate_post_title],
    )
    pub_date = models.DateTimeField("작성날짜", default=timezone.now)
    modify_date = models.DateTimeField("수정날짜", null=True, blank=True)
    content = models.TextField("포스트 내용", validators=[validate_post_content])
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="posts"
    )

    def __str__(self):
        return self.postTitle
