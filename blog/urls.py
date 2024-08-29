from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path("", views.main, name="index"),
    path("post/<int:post_id>/", views.post_view, name="post_detail"),
]
