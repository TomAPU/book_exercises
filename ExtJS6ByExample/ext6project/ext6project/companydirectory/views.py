from django.shortcuts import render
from django.views.generic.base import TemplateView
from braces.views import JSONResponseMixin
from django.views.generic.list import ListView
from django.views.generic.detail import SingleObjectMixin, DetailView

from .models import Employee

from .serializers import EmployeeSerializer
from rest_framework import generics


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Create your views here.
class IndexView(TemplateView):

    template_name = "companydirectory/index.html"
