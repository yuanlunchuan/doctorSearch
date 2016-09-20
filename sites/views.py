from django.shortcuts import render
import logging

logger = logging.getLogger('doctors.views')

def index(request):
  return render(request, 'sites/index.html', locals())
