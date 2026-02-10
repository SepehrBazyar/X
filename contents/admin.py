from datetime import timedelta

from django.contrib import admin, messages
from django.db.models import QuerySet
from django.http import HttpRequest
from django.utils import timezone

from contents.choices import PostStates
from contents.models import (
    Comment,
    Post,
    PostPhoto,
    Tag,
    QuotePost,
)

# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "slug",
        "name",
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = (
        "title",
        "body",
        "state",
        "created_at",
        "tag_names",
    )
    readonly_fields = (
        "created_at",
        "tag_names",
        "state",
    )
    list_display = (
        "id",
        "title",
        "state",
        "is_recent_post",
    )
    list_filter = (
        "state",
    )
    search_fields = (
        "title",
        "id",
    )
    actions = (
        "publish_post",
    )

    @admin.display(
        boolean=True,
        description="Is Recent??",
    )
    def is_recent_post(self, obj: Post):
        return (timezone.now() - obj.created_at) <= timedelta(days=3)

    @admin.action(description="Publish Selected Post")
    def publish_post(self, request: HttpRequest, queryset: QuerySet[Post]):
        queryset.update(state=PostStates.PUBLISHED)
        self.message_user(request, "PUBLISHED POSTS OR POST", messages.SUCCESS)

    # publish_post.short_description = "Publish Selected Post"


# admin.site.register(Comment)
# admin.site.register(Post)
# admin.site.register(PostPhoto)
# admin.site.register(Tag, TagAdmin)
# admin.site.register(QuotePost)
