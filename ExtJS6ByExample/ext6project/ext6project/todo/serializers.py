from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    desc = serializers.CharField(required=True, allow_blank=False, max_length=255)
    done = serializers.BooleanField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Todo` instance, given the validated data.
        """
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Todo` instance, given the validated data.
        """
        instance.desc = validated_data.get('desc', instance.title)
        instance.done = validated_data.get('done', instance.done)
        instance.save()
        return instance
