from django.db import models
from django.db.models.base import Model
from django.utils.timezone import datetime

# Create your models here.

class Url(models.Model):
    url = models.CharField(max_length=1000)
    uuid = models.CharField(max_length=20)
    owner = models.ForeignKey('auth.User', related_name='urls', on_delete=models.CASCADE,default=datetime.now)

    def save(self, *args, **kwargs):
        super(Url, self).save(*args, **kwargs)
