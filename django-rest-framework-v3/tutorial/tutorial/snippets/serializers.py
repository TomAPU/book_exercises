from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Snippet

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-hightlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'hightlight', 'owner',
                'title', 'code', 'linenos', 'language', 'style',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedIdentityField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets',)
