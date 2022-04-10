"""edebou URL Configuration

"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('api/',include('myApp.urls')),
    path('admin/', admin.site.urls)
]
