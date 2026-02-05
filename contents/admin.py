from django.contrib import admin

from contents.models import (
    Comment,
    Post,
    PostPhoto,
    Tag,
    QuotePost,
)

# Register your models here.
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(PostPhoto)
admin.site.register(Tag)
admin.site.register(QuotePost)
