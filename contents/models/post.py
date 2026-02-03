from django.db import models
# from django.contrib.postgres.fields import ArrayField

from contents.choices import PostStates


class Tag(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=16)


class Post(models.Model):
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


class PostPhoto(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="photos",
    )
    photo = models.FileField(
        upload_to="headers/"
    )


class Comment(models.Model):
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
