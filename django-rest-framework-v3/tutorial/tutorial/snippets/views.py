from rest_framework import generics

from .models import Snippet
from .serializers import SnippetSerializer

# A view that supports listing all the existing snippets, or creating a new snippet.
class SnippetList(generics.ListCreateAPIView):
    """
    List all code snippets, or create a new one.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

# A view that corresponds to an individual snippet, can be used to
# retrieve, update or delete the snippet.
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code snippet.
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
