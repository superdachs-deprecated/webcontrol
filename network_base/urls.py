from django.conf.urls import patterns, url
from network_base import views

urlpatterns = patterns('',
    url(r'^$', views.index,name='network_base'),
)
