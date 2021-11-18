from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from serviexpress_api.models import PurchaseOrder
from .ser_enterprise import EnterpriseSerializer
from .ser_employee import EmployeeSerializer
from .ser_provider import ProviderSerializer
from .ser_currency import CurrencySerializer
from .ser_purchase_order_detail import PurchaseOrderDetailSerializer


class PurchaseOrderSerializer(FlexFieldsModelSerializer):
    enterprise = serializers.PrimaryKeyRelatedField(read_only=True)
    employee = serializers.PrimaryKeyRelatedField(read_only=True)
    provider = serializers.PrimaryKeyRelatedField(read_only=True)
    currency = serializers.PrimaryKeyRelatedField(read_only=True)
    details = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = PurchaseOrder
        fields = "__all__"

    expandable_fields = {
        'enterprise': EnterpriseSerializer,
        'employee': EmployeeSerializer,
        'provider': ProviderSerializer,
        'currency': CurrencySerializer,
        'details': (PurchaseOrderDetailSerializer, {'many': True})
    }