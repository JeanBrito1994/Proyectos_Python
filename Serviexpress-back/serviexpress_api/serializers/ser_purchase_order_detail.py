from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from serviexpress_api.models import PurchaseOrderDetail
from .ser_product import ProductSerializer


class PurchaseOrderDetailSerializer(FlexFieldsModelSerializer):
    product = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = PurchaseOrderDetail
        fields = "__all__"

    expandable_fields = {
        'product': ProductSerializer
    }
