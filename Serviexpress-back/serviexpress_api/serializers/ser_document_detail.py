from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from serviexpress_api.models import DocumentDetail
from .ser_product import ProductSerializer


class DocumentDetailSerializer(FlexFieldsModelSerializer):
    # product = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = DocumentDetail
        fields = "__all__"

    expandable_fields = {
        'product': ProductSerializer
    }
