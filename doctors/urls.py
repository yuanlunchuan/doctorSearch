from django.conf.urls import url
from doctors import views, doctors

urlpatterns = [
    url(r'^', doctors.index, name='doctors_index'),
    url(r'^show$', doctors.show, name='doctor_show'),
]
