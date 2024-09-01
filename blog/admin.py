from django.contrib import admin
from blog.models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]


class BlogAdmin(admin.ModelAdmin):
    list_display = ["id", "postTitle", "pub_date", "get_category"]
    list_filter = ["pub_date", "category"]
    search_fields = ["postTitle", "content"]

    def get_category(self, obj):
        return obj.category.name if obj.category else "-"

    get_category.short_description = "Category"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, BlogAdmin)
