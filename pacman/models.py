from django.db import models

class Repository(models.model):
    name = models.CharField(max_length=10)
    url = models.URLField(max_length=200)
    isActive = models.BooleanField()
