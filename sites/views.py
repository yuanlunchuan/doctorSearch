from django.shortcuts import render

def index(request):
  return render(request, 'sites/index.html', locals())
