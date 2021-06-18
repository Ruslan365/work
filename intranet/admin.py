"""
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
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
"""
"""

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "email",
        "last_login_at",
    ]
    readonly_fields = ("password", "created_at", "last_login_at")

"""
"""

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "author", "created_at", "updated_at"]
    readonly_fields = ("created_at", "updated_at")


admin.site.register(Tag)
admin.site.register(LikeDislike)
"""
