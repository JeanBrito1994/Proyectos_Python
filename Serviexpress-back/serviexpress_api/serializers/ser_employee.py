from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from serviexpress_api.models import User, Employee
from .ser_user import UserSerializer


class EmployeeSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    expandable_fields = {
        'user': UserSerializer
    }

    def create(self, validated_data):
        instance = Employee.objects.create(**validated_data)
        instance.save()
        user = instance.user
        user.is_staff = True
        user.save()
        return instance

    def update(self,instance, validated_data):
        instance = super().update(instance,validated_data)
        user = instance.user
        user.is_staff = True
        user.save()
        return instance