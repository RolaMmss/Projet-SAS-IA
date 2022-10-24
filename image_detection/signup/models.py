from django.db import models

class User(models.Model):
    name = models.fields.CharField(max_length=100)
    age = models.fields.IntegerField()
    email = models.fields.CharField(max_length=100)
    mdp = models.fields.CharField(max_length=100)