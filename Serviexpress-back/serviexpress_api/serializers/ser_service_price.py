from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from serviexpress_api.models import ServicePrice
from .ser_currency import CurrencySerializer


class ServicePriceSerializer(FlexFieldsModelSerializer):

    currency = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = ServicePrice
        fields =  '__all__'

    expandable_fields = {
        'currency': CurrencySerializer
    }