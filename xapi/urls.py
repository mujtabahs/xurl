from django.conf.urls import url
from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from xapi import views

urlpatterns = [
    path('urls/', views.UrlList.as_view()),
    path('urls/<int:pk>', views.UrlDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
   
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]