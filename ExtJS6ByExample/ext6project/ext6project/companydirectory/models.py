#-*- encoding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.
@python_2_unicode_compatible
class Employee(models.Model):
    first_name = models.CharField("First Name", max_length=20, blank=False, null=False)
    last_name = models.CharField("Last Name", max_length=20, blank=False, null=False)
    email = models.CharField("Email", max_length=255, blank=False, null=False)
    address = models.CharField("Address", max_length=255, blank=False, null=False)
    city = models.CharField("City", max_length=20, blank=False, null=False)
    state = models.CharField("State", max_length=20, blank=False, null=False)
    work_type = models.CharField("Type", max_length=20, blank=False, null=False)
    phone = models.CharField("Phone Number", max_length=20, blank=False, null=False)

    def __str__(self):
        return self.first_name + self.last_name
