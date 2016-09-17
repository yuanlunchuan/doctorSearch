from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin

urlpatterns = [
  url(r'^uploads/hospital/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
  url(r'^', include('sites.urls')),
  url(r'^admin/', admin.site.urls),
  url(r'^doctors/', include('doctors.urls')),
]
