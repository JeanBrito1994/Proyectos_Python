from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from serviexpress_api.models import ProductCategory
from .ser_enterprise import EnterpriseSerializer


class ProductCategorySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"
