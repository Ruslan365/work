from django.contrib import admin
from .models import Post, Comment, Tag, LikeDislike
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", "author_id", "created_at", "is_published")
    list_filter = ("is_published", "created_at", "author_id")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("author_id",)
    date_hierarchy = "created_at"
    ordering = ("is_published", "created_at")
    readonly_fields = (
        "created_at",
        "published_at",
    )
    summernote_fields = ("body")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "author", "created_at", "updated_at"]
    readonly_fields = ("created_at", "updated_at")


admin.site.register(Tag)
admin.site.register(LikeDislike)
