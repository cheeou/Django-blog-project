from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse
from blog.models import Post, Category
from blog.forms import PostForm


@login_required
def post_add(request):  # 글작성
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("blog:post_detail", post_id=post.id)
    else:
        form = PostForm()
    return render(request, "blog/post_add.html", {"form": form})


# @login_required
# def post_add(request):  # 글작성
#     if request.method == "POST":
#         if "action" in request.POST and request.POST["action"] == "cancel":
#             return redirect("blog:post_list")  # 또는 적절한 URL로 리다이렉트
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect("blog:post_detail", post_id=post.id)
#     else:
#         form = PostForm()
#     return render(request, "blog/post_add.html", {"form": form})


def post_detail(request, post_id):  # 상세글
    post_detail = get_object_or_404(Post, pk=post_id)
    category = post_detail.category

    # 작성자의 프로필 이미지 가져오기
    author_profile_image = (
        post_detail.author.profile_image
        if hasattr(post_detail.author, "profile_image")
        else None
    )

    context = {
        "post_detail": post_detail,
        "category": category,
        "author_profile_image": author_profile_image,
    }

    return render(request, "blog/post_detail.html", context)


def post_edit(request, post_id):  # 글수정- 기존 글 불러오기
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "blog/post_edit.html", {"post": post})


def post_update(request, post_id):  # 글 수정 - 수정 내용 업데이트
    update_posting = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        update_posting.postTitle = request.POST["postTitle"]
        update_posting.content = request.POST["content"]
        update_posting.modify_date = timezone.now()
        update_posting.save()
        return redirect("blog:post_detail", post_id=update_posting.id)
    return render(request, "blog/post_edit.html", {"post": update_posting})


def post_delete(request, post_id):  # 글 삭제
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        post.delete()
        return redirect(reverse("main:main"))
    return render(request, "blog/post_confirm_delete.html", {"post": post})
