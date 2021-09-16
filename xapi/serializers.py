from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.relations import ManyRelatedField
from xapi.models import Url
from django.contrib.auth.models import User

# Using model serializers 
class XapiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ['url', 'uuid', 'owner'] 
    owner = serializers.ReadOnlyField(source='owner.username')

class UserSerializer(serializers.ModelSerializer):
    urls = serializers.PrimaryKeyRelatedField(many=True, queryset = Url.objects.all() )
    class Meta:
        model = User
        fields = ['id', 'username', 'urls']
