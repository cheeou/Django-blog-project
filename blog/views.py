from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from blog.forms import PostForm


def main(request):  # 메인 화면
    posts = Post.objects.all()

    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)


def post_detail(request, post_id):  # 상세글
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, "blog/post_detail.html", {"post_detail": post_detail})


def post_add(request):  # 글작성
    if request.method == "POST":
        if "cancel" in request.POST:
            return redirect("blog:index")
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect("blog:post_detail", post_id=post.id)
    else:
        form = PostForm()
    return render(request, "blog/post_add.html", {"form": form})
