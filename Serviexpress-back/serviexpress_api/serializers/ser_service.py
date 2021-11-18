from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from serviexpress_api.models import Service, ServicePrice
from .ser_service_type import ServiceTypeSerializer
from .ser_service_price import ServicePriceSerializer
from .ser_enterprise import EnterpriseSerializer


class ServiceSerializer(FlexFieldsModelSerializer):
    service_type = serializers.PrimaryKeyRelatedField(read_only=True)
    enterprise = serializers.PrimaryKeyRelatedField(read_only=True)
    price = serializers.SerializerMethodField(method_name='get_price')

    def get_price(self,obj):
        service_price = ServicePrice.objects.get(service=obj,currency=obj.enterprise.currency_default)
        return service_price.price
    class Meta:
        model = Service
        fields = '__all__'
    
    expandable_fields = {
        'service_type': ServiceTypeSerializer,
        'enterprise': EnterpriseSerializer
    }