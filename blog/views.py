from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse
from blog.models import Post
from blog.forms import PostForm


def post_add(request):  # 글작성
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect("blog:post_detail", post_id=post.id)
    else:
        form = PostForm()
    return render(request, "blog/post_add.html", {"form": form})


def post_detail(request, post_id):  # 상세글
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, "blog/post_detail.html", {"post_detail": post_detail})


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
