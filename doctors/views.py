import logging
from django.shortcuts import render

logger = logging.getLogger('doctors.views')

def index(request):
  return render(request, 'doctors/index1.html', locals())

def show(request, doctor_id="0"):
  return render(request, 'doctors/show2.html', locals())
