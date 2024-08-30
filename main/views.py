from django.shortcuts import render
from blog.models import Post


def main(request):  # 메인 화면
    posts = Post.objects.all()

    context = {
        "posts": posts,
    }
    return render(request, "main/index.html", context)
