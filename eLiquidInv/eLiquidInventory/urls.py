from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^eliquid/(?P<eliquid_id>[0-9]+)/$', views.eliquid, name='eliquid'),
]