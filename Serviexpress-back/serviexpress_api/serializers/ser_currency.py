from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from serviexpress_api.models import Currency


class CurrencySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"