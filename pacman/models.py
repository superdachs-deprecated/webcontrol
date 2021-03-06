from django.db import models

class Repository_Distribution(models.Model):
    repository = models.ForeignKey('Repository')
    distribution = models.ForeignKey('Distribution')

class Distribution(models.Model):
    name = models.CharField(max_length=200)

class Repository(models.Model):
    name = models.CharField(max_length=200)
    repourl = models.CharField(max_length=200)
    isActive = models.BooleanField()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
