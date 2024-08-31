from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path("post/add/", views.post_add, name="post_add"),
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
    path("post/edit/<int:post_id>/", views.post_edit, name="post_edit"),
    path("post/update/<int:post_id>/", views.post_update, name="post_update"),
    path("post/delete/<int:post_id>/", views.post_delete, name="post_delete"),
]
