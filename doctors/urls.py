from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='doctors_index'),
    url(r'^(?P<doctor_id>[0-9]+)/$', views.show, name='doctors_show')
]
