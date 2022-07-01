import uuid
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Artefact(BaseModel):
    title = models.CharField(max_length=256)
    country = models.CharField(max_length=128, null=True)
    description = models.CharField(max_length=512, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "artefact"
        verbose_name_plural = "artefacts"
