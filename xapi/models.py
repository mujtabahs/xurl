from django.db import models
from django.db.models.base import Model

# Create your models here.

class Url(models.Model):
    url = models.CharField(max_length=1000)
    uuid = models.CharField(max_length=20)
