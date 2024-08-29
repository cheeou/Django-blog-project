from django.shortcuts import render, get_object_or_404
from blog.models import Post


def main(request):  # 메인 화면
    posts = Post.objects.all()

    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)


def post_view(request, post_id):  # 상세글
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, "blog/post-view.html", {"post_detail": post_detail})
