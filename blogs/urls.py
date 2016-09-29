from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name = 'blog_index'),
  url(r'^(?P<blog_id>[0-9]+)/$', views.show, name='blog_show')
]