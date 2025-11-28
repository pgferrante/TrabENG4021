from django.contrib import admin
from django.urls import path, include
from CarsApp import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CarsApp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]