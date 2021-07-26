from django.contrib import admin
from django.urls import path
from . import views
from . import api

app_name = "job"

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('add', views.add_job, name='add_job'),
    path('<str:slug>', views.job_detail, name='job_detail'),

    ## api
    path('api/joblist', api.joblist_api, name='joblist_api'),
]
