from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=True, allow_blank=False,
            max_length=20)
    last_name = serializers.CharField(required=True, allow_blank=False,
            max_length=20)
    email = serializers.CharField(required=True, allow_blank=False, max_length=255)
    address = serializers.CharField(required=True, allow_blank=False, max_length=255)
    city = serializers.CharField(required=True, allow_blank=False,
            max_length=20)
    state = serializers.CharField(required=True, allow_blank=False,
            max_length=20)
    work_type = serializers.CharField(required=True, allow_blank=False,
            max_length=20)
    phone = serializers.CharField(required=True, allow_blank=False,
            max_length=20)

    def create(self, validated_data):
        """
        Create and return a new `Employee` instance, given the validated data.
        """
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Employee` instance, given the validated data.
        """
        instance.first_name = validated_data.get('first_name',
                instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.address = validated_data.get('address', instance.address)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.work_type = validated_data.get('work_type', instance.work_type)
        instance.phone = validated_data.get('phone', instance.phone)

        instance.save()
        return instance
