from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from serviexpress_api.models import Provider


class ProviderSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Provider
        fields = "__all__"