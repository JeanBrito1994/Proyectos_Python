from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from serviexpress_api.models import Enterprise, Currency
from .ser_currency import CurrencySerializer


class EnterpriseSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Enterprise
        fields = "__all__"
    
    expandable_fields = {
        'currency_default': CurrencySerializer
    }