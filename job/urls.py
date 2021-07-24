from django.contrib import admin
from django.urls import path
from . import views

app_name = "job"

urlpatterns = [
    path('', views.job_list),
    path('<str:slug>', views.job_detail, name='job_detail'),
]