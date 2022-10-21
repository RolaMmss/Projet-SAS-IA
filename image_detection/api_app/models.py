from django.db import models

# Create your models here.

class ApiKeywordsModel(models.Model):
    url = models.URLField(
        max_length=100,
        blank=False,
        null=True,
    )

    num_keywords = models.IntegerField(
        blank=False,
        null=True
    )