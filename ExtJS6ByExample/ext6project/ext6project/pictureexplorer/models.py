#-*- encoding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.
@python_2_unicode_compatible
class Pic(models.Model):
    url = models.CharField("URL", max_length=255, blank=False, null=False)
    albumId = models.IntegerField("Album ID", blank=False, null=False)

    def __str__(self):
        return self.url
