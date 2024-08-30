from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
    path("post/add/", views.post_add, name="post_add"),
]
