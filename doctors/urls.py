from django.conf.urls import url
from doctors import views, doctors

urlpatterns = [
    url(r'^', doctors.index, name='doctors_index'),
    url(r'^(?P<doctor_id>[0-9]+)/$', doctors.show, name='doctors_show'),
]
