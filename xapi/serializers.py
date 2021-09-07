from django.db import models
from django.db.models import fields
from rest_framework import serializers
from xapi.models import Url

# Using model serializers 
class XapiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ['url', 'uuid'] 