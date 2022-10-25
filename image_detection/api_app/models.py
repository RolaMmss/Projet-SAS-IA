from hashlib import blake2b
from django.db import models

# Create your models here.

class ApiModel(models.Model):
    url = models.URLField(
        max_length=100,
        blank=False,
        null=True,
    )


    # num_keywords = models.IntegerField(
    #     blank=False,
    #     null=True
    # )
    
    # CHOICES = [
    #     ('s1',"s1"),
    #     ('s2',"s2"),
    #     ('s3',"s3"),
    # ]

    # api_choices = models.CharField(
    #     max_length=50,
    #     blank=False,
    #     choices = CHOICES,
    # )