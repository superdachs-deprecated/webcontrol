from django.db import models

class Distribution(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Repository(models.Model):
    name = models.CharField(max_length=10)
    url = models.URLField(max_length=200)
    isActive = models.BooleanField()
    distribution = models.ForeignKey(Distribution)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
