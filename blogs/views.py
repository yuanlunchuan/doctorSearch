from django.shortcuts import render

def index(request):
  return render(request, 'blogs/index.html', {})

def show(request, blog_id="0"):
  return render(request, 'blogs/show.html', {})
