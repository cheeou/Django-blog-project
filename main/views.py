from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Count
from blog.models import Post, Category


def index(request):
    return render(request, "main/index.html")


# def main(request):
#     # 카테고리
#     # 내가 쓴 글 보기
#     show_my_posts = request.GET.get("show_my_posts") == "true"

#     if show_my_posts and request.user.is_authenticated:
#         post_list = Post.objects.filter(author=request.user).order_by("-pub_date")
#     else:
#         post_list = Post.objects.all().order_by("-pub_date")

#     # pagination
#     paginator = Paginator(post_list, 6)  # 한 페이지에 6개 출력
#     page_number = request.GET.get("page")
#     posts = paginator.get_page(page_number)

#     if request.user.is_authenticated:
#         user_profile = request.user
#     else:
#         user_profile = None

#     context = {
#         "posts": posts,
#         "show_my_posts": show_my_posts,
#         "user_profile": user_profile,
#     }

#     return render(request, "main/main.html", context)


def main(request):
    # 카테고리 가져오기
    categories = Category.objects.all()

    # 내가 쓴 글 보기
    show_my_posts = request.GET.get("show_my_posts") == "true"

    if show_my_posts and request.user.is_authenticated:
        post_list = Post.objects.filter(author=request.user).order_by("-pub_date")
    else:
        post_list = Post.objects.all().order_by("-pub_date")

    # 선택된 카테고리로 필터링
    selected_category = request.GET.get("category")
    if selected_category:
        post_list = post_list.filter(category__id=selected_category)

    # pagination
    paginator = Paginator(post_list, 6)  # 한 페이지에 6개 출력
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)

    if request.user.is_authenticated:
        user_profile = request.user
        # 사용자가 작성한 글의 카테고리만 가져오기
        user_categories = (
            Category.objects.filter(posts__author=request.user)
            .annotate(post_count=Count("posts"))
            .distinct()
        )
        print("User categories:", user_categories)  # 디버깅용 출력
    else:
        user_profile = None
        user_categories = []

    context = {
        "posts": posts,
        "show_my_posts": show_my_posts,
        "user_profile": user_profile,
        "categories": categories,  # 모든 카테고리 목록
        "user_categories": user_categories,  # 사용자가 작성한 글의 카테고리 목록
        "selected_category": selected_category,  # 선택된 카테고리 추가
    }

    return render(request, "main/main.html", context)
