from django.shortcuts import render

def index(request):
  print("----------in blogs index")
  return render(request, 'blogs/index.html', {})
