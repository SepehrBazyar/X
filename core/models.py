from django.db import models

# Create your models here.
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def archive(self):
        return super().get_queryset().filter(is_deleted=True)


class BaseModel(models.Model):
    class Meta:
        abstract = True

    objects = CustomManager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(
        default=False,
        db_index=True,
    )

    def delete(self, using = ..., keep_parents = ...):
        self.is_deleted = True
        self.save()
