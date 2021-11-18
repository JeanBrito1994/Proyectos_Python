from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from serviexpress_api.models import User, Client
from .ser_user import UserSerializer
from .ser_city import CitySerializer


class ClientSerializer(FlexFieldsModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    city = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Client
        fields = "__all__"

    expandable_fields = { 
        'user': UserSerializer,
        'city': CitySerializer
    }