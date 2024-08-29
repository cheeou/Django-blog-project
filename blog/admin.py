from django.contrib import admin
from blog.models import Post


class BlogAdmin(admin.ModelAdmin):
    list_display = ["id", "postTitle", "pub_date"]


admin.site.register(Post, BlogAdmin)
