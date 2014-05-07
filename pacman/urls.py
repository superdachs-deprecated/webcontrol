from django.conf.urls import patterns, url
from pacman import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='pacman'),
)
