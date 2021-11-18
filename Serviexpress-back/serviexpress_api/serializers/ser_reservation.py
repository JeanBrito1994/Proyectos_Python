from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from serviexpress_api.models import Reservation
from .ser_client import ClientSerializer
from .ser_service import ServiceSerializer
from .ser_enterprise import EnterpriseSerializer


class ReservationSerializer(FlexFieldsModelSerializer):
    client = serializers.PrimaryKeyRelatedField(read_only=True)
    
    enterprise = serializers.PrimaryKeyRelatedField(read_only=True)
    status = serializers.CharField(source='get_status_display')
    class Meta:
        model = Reservation
        fields = "__all__"

    expandable_fields = {
        'client': ClientSerializer,
        'services': (ServiceSerializer, {'many': True}),
        'enterprise': EnterpriseSerializer
    }