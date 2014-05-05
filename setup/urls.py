from django.conf.urls import patterns, url
from setup import views

urlpatterns = patterns('',
    url(r'^firststart/', views.firststart, name='firststart'),
)
