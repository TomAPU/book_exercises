from django.shortcuts import render
from django.views.generic.base import TemplateView
from braces.views import JSONResponseMixin
from django.views.generic.list import ListView
from django.views.generic.detail import SingleObjectMixin, DetailView

from .models import Todo

from .serializers import TodoSerializer
from rest_framework import generics


class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# Create your views here.
class IndexView(TemplateView):

    template_name = "todo/index.html"
