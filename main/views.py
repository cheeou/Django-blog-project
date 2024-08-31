from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post


def index(request):
    return render(request, "main/index.html")


def main(request):  # 메인 화면
    posts = Post.objects.all()

    context = {
        "posts": posts,
    }
    return render(request, "main/main.html", context)
