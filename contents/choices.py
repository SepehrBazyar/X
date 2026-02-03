from django.db import models


class PostStates(models.TextChoices):
    DRAFT = "d", "Draft"
    APPROVED = "a", "Approved"
    PUBLISHED = "p", "Published"
