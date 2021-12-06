from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('login', include('login.urls')),
    path('main', include('main.urls')),
    path('api', include('myapi.urls')),
]
