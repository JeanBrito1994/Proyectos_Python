from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from serviexpress_api.models import ProductPrice
from .ser_currency import CurrencySerializer
from .ser_product import ProductSerializer


class ProductPriceSerializer(FlexFieldsModelSerializer):
    currency = serializers.PrimaryKeyRelatedField(read_only=True)
    product = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = ProductPrice
        fields = "__all__"
    
    expandable_fields = {
        'currency': CurrencySerializer,
        'product': ProductSerializer
    }