from django.shortcuts import render
from diseases.models import *
import logging

logger = logging.getLogger('doctors.views')

def index(request):
  diseases_categories = DiseaseCategory.objects.all()
  return render(request, 'sites/index.html', locals())
