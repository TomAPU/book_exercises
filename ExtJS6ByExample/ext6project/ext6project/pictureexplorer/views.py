from django.views.generic.base import TemplateView

from .models import Pic

from .serializers import PicSerializer
from rest_framework import viewsets


class PicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pic.objects.all()
    serializer_class = PicSerializer

# Create your views here.
class IndexView(TemplateView):

    template_name = "pictureexplorer/index.html"
