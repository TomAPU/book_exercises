from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from django.contrib.auth.models import User

from .models import Snippet
from .serializers import SnippetSerializer
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly


@api_view(['GET',])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format),
    })

# A view that supports listing all the existing snippets, or creating a new snippet.
class SnippetList(generics.ListCreateAPIView):
    """
    List all code snippets, or create a new one.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# A view that corresponds to an individual snippet, can be used to
# retrieve, update or delete the snippet.
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code snippet.
    """

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer, )

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
