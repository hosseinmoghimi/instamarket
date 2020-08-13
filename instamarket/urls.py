
from django.contrib import admin
from django.urls import path,include



from .settings import MEDIA_URL,MEDIA_ROOT,STATIC_URL,STATIC_ROOT
from django.views.static import serve 
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('dashboard.urls')),


    url(r'^'+MEDIA_URL[1:]+'(?P<path>.*)$', serve,{'document_root': MEDIA_ROOT}), 
    url(r'^'+STATIC_URL[1:]+'(?P<path>.*)$', serve,{'document_root': STATIC_ROOT}),  
]


