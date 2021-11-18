from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from serviexpress_api.models import Document
from .ser_enterprise import EnterpriseSerializer
from .ser_employee import EmployeeSerializer
from .ser_client import ClientSerializer
from .ser_currency import CurrencySerializer
from .ser_document_detail import DocumentDetailSerializer


class DocumentSerializer(FlexFieldsModelSerializer):
    # enterprise = serializers.PrimaryKeyRelatedField(read_only=True)
    # currency = serializers.PrimaryKeyRelatedField(read_only=True)
    # employee = serializers.PrimaryKeyRelatedField(read_only=True)
    # client = serializers.PrimaryKeyRelatedField(read_only=True)
    # services = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    document_type = serializers.CharField(source='get_document_type_display')

    class Meta:
        model = Document
        fields = "__all__"

    expandable_fields = {
        'enterprise': EnterpriseSerializer,
        'currency': CurrencySerializer,
        'employee': EmployeeSerializer,
        'client': ClientSerializer,
        'details': (DocumentDetailSerializer, {'many': True})
    }