from django.shortcuts import render

def index(request):
  return render(request, 'doctors/index.html', locals())

def show(request, doctor_id="0"):
  return render(request, 'doctors/show.html', locals())
