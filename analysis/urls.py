from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    #path('',views.upload_file, name='upload_file'),
     path('upload/', views.upload_file, name='upload_file'),
    path('results/', views.results, name='results'),
]