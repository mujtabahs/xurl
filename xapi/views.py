# from xurls.xapi.permissions import IsOwnerOrReadOnly
from xapi.serializers import UserSerializer
from xapi.serializers import XapiSerializer
from django.shortcuts import render, resolve_url
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from xapi.models import Url
from xapi.serializers import XapiSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions

from xapi.permissions import IsOwnerOrReadOnly

# # @csrf_exempt
# @api_view(['GET', 'POST'])
# def xapi_list(request,self):
#     if request.method == 'GET':
#         urls = Url.objects.all()
#         serializer = XapiSerializer(urls, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = XapiSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save(owner = self.request.user)
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # @csrf_exempt
# @api_view(['GET', 'PUT', 'DELETE'])
# def url_details(request,pk):
#     try: 
#         url = Url.objects.get(pk=pk)
#     except Url.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = XapiSerializer(url)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = XapiSerializer(url, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class UrlList(generics.ListCreateAPIView):
    queryset = Url.objects.all()
    serializer_class = XapiSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        owner_queryset = self.queryset.filter(owner = self.request.user)
        return owner_queryset

class UrlDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Url.objects.all()
    serializer_class = XapiSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(owner = self.request.user)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


