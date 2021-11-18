from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from serviexpress_api.models import City


class CitySerializer(FlexFieldsModelSerializer):

    class Meta:
        model = City
        fields = "__all__"
