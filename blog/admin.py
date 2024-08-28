from django.contrib import admin
from blog.models import Post, Comment


@admin.register(Post, Comment)
class PersonAdmin(admin.ModelAdmin):
    pass
