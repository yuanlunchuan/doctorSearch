from django.conf.urls import url
from doctors import views, doctors

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^doctors/$', doctors.show, name='doctor_show')
]
