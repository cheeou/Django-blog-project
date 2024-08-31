from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post


def index(request):
    return render(request, "main/index.html")


# def main(request):  # 메인 화면
#     posts = Post.objects.all()


#     context = {
#         "posts": posts,
#     }
#     return render(request, "main/main.html", context)
def main(request):
    show_my_posts = request.GET.get("show_my_posts") == "true"

    if show_my_posts and request.user.is_authenticated:
        posts = Post.objects.filter(author=request.user).order_by("-pub_date")
    else:
        posts = Post.objects.all().order_by("-pub_date")

    context = {"posts": posts, "show_my_posts": show_my_posts}
    return render(request, "main/main.html", context)
