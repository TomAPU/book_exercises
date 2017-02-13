#-*- encoding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.
@python_2_unicode_compatible
class Todo(models.Model):
    desc = models.CharField("描述", max_length=255, blank=False, null=False)
    done = models.BooleanField("完成状态", default=False)

    def __str__(self):
        return self.desc

    def to_dict(self):
        return {
            'id': self.id,
            'desc': self.desc,
            'done': self.done,
        }
