from django.db import models
from django.utils import timezone
from utils.validators import validate_post_title, validate_post_content


class Post(models.Model):
    postTitle = models.CharField(
        "포스트 제목",
        max_length=50,
        validators=[validate_post_title],
    )
    pub_date = models.DateTimeField("작성날짜", default=timezone.now)
    modify_date = models.DateTimeField("수정날짜", null=True, blank=True)
    content = models.TextField("포스트 내용", validators=[validate_post_content])

    def __str__(self):
        return self.postTitle
