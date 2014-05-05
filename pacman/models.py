from django.db import models

class Distribution(models.Model):
    name = models.CharField(max_length=40)

class Repository(models.Model):
    name = models.CharField(max_length=10)
    url = models.URLField(max_length=200)
    isActive = models.BooleanField()
    distribution = models.ForeignKey(Distribution)
