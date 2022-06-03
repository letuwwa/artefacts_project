from django.db import models


class Artefact(models.Model):
    title = models.CharField(max_length=256)
    country = models.CharField(max_length=128, null=True)
    description = models.CharField(max_length=512, null=True)

    def __str__(self):
        return self.title
