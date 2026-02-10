from django.db import models
# from django.contrib.postgres.fields import ArrayField

from core.models import BaseModel
from contents.choices import PostStates


class Tag(BaseModel):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=16)


class Post(BaseModel):
    title = models.CharField(
        max_length=32,
        verbose_name="Title",
        help_text="Title of Post",
        db_column="name",
    )
    body = models.TextField(
        null=True,
        blank=True,
        verbose_name="Body of Content",
        help_text="Full Content of this Post",
    )
    tags = models.ManyToManyField(
        Tag,
        related_name="posts",
    )
    state = models.CharField(
        max_length=1,
        choices=PostStates.choices,
        default=PostStates.DRAFT,
    )

    @property
    def tag_names(self):
        names = [tag.name for tag in self.tags.all()]
        return " - ".join(names)

    def __str__(self):
        return f"{self.id}) {self.title}"


class QuotePost(Post):
    quote = models.URLField()


class RecentPost(Post):
    class Meta:
        proxy = True

    @property
    def comments_count(self):
        return self.comments.count()


class PostPhoto(BaseModel):
    class Meta:
        db_table = "media"
        verbose_name = "Media"
        verbose_name_plural = "Medias"
        ordering = (
            "-id",
        )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="photos",
    )
    photo = models.FileField(
        upload_to="headers/"
    )


class Comment(BaseModel):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    text = models.TextField()
    reply_to = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
    )
