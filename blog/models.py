from django.db import models
from django.utils import timezone


class Post(models.Model):
    postTitle = models.CharField("포스트 제목", max_length=100, default="")
    pub_date = models.DateTimeField("작성날짜", null=True)
    content = models.TextField("포스트 내용")

    def __str__(self):
        return self.postTitle


class PostImage(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name="포스트",
        on_delete=models.CASCADE,
    )
    photo = models.ImageField("포스트 이미지", upload_to="post/")

    def __str__(self):
        return f"{self.post.title}의 이미지 (ID: {self.id})"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField("댓글 내용")

    def __str__(self):
        return f"{self.post.title}의 댓글 (ID: {self.id})"
