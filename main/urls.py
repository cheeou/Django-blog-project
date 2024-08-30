from django.urls import path
from main import views
from django.contrib.auth import views as auth_views_index

app_name = "main"


urlpatterns = [
    path(
        "",
        auth_views_index.LoginView.as_view(template_name="main/index.html"),
        name="index_login",
    ),
    path("main/", views.main, name="main"),
]
