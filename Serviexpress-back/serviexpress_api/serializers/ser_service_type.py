from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from serviexpress_api.models import ServiceType
from .ser_enterprise import EnterpriseSerializer


class ServiceTypeSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ServiceType
        fields = "__all__"
    
    expandable_fields = {
        'enterprise': EnterpriseSerializer
    }