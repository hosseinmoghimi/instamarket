
from django.contrib import admin
from django.urls import path,include



from .settings import MEDIA_URL,MEDIA_ROOT,STATIC_URL,STATIC_ROOT
from django.views.static import serve 
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('dashboard.urls')),
    path('project_manager/',include('manager.urls')),


    url(r'^media/(?P<path>.*)$', serve,{'document_root': MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': STATIC_ROOT}),  
]


