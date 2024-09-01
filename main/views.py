from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post


def index(request):
    return render(request, "main/index.html")


def main(request):
    # 내가 쓴 글 보기
    show_my_posts = request.GET.get("show_my_posts") == "true"

    if show_my_posts and request.user.is_authenticated:
        post_list = Post.objects.filter(author=request.user).order_by("-pub_date")
    else:
        post_list = Post.objects.all().order_by("-pub_date")

    # pagination
    paginator = Paginator(post_list, 6)  # 한 페이지에 6개 출력
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)

    context = {"posts": posts, "show_my_posts": show_my_posts}

    return render(request, "main/main.html", context)
