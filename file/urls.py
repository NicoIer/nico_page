from django.contrib import admin
from django.urls import path

from file import views

urlpatterns = [
    path('', views.file_home_page, name='file_home_page')
]
