from django.db import models

class User(models.Model):
    lastname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    posix_account_name = models.CharField(max_length=200)
    posix_account_passwd = models.CharField(max_length=200)
    home = models.CharField(max_length=200)
    shell = models.CharField(max_length=200)

class Group(models.Model):
    group_name = models.CharField(max_length=200)
    group_description = models.TextField()

class User_Group(models.Model):
    user = models.ForeignKey('User')
    group = models.ForeignKey('Group')
