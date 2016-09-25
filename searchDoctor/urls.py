from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin

#  url(r'^uploads/hospital/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
urlpatterns = [
  url(r'^', include('sites.urls')),
  url(r'^admin/', admin.site.urls),
  url(r'^doctors/', include('doctors.urls')),
  url(r'^blogs/', include('blogs.urls')),
]
