from django.contrib import admin
from pacman.models import Distribution
from pacman.models import Repository

admin.site.register(Distribution)
admin.site.register(Repository)

