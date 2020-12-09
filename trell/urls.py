from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^movies/', include('movies.urls')),
    url(r'^', include('movies.urls')),
    
]
