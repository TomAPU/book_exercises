from django.views.generic.base import TemplateView

from .models import Employee

from .serializers import EmployeeSerializer
from rest_framework import viewsets


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Create your views here.
class IndexView(TemplateView):

    template_name = "companydirectory/index.html"
