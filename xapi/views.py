from django.shortcuts import render, resolve_url
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from xapi.models import Url
from xapi.serializers import XapiSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['GET', 'POST'])
def xapi_list(request):
    if request.method == 'GET':
        urls = Url.objects.all()
        serializer = XapiSerializer(urls, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = XapiSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

