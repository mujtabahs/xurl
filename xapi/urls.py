from django.conf.urls import url
from django.urls import path
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from xapi import views

urlpatterns = [
    path('xapi/', views.xapi_list),
    path('xapi/<int:pk>', views.url_details)
   
]

urlpatterns = format_suffix_patterns(urlpatterns)