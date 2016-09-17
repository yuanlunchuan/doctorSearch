from django.conf.urls import url
from doctors import views, doctors

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^doctors', doctors.index, name='doctors_index'),
    url(r'^doctors/show$', doctors.show, name='doctor_show'),
]
