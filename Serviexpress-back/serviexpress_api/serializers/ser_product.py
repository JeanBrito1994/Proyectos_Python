from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from serviexpress_api.models import Product, ProductPrice
from .ser_provider import ProviderSerializer
from .ser_product_category import ProductCategorySerializer
from .ser_enterprise import EnterpriseSerializer


class ProductSerializer(FlexFieldsModelSerializer):
    provider = serializers.PrimaryKeyRelatedField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(read_only=True)
    enterprise = serializers.PrimaryKeyRelatedField(read_only=True)
    price = serializers.SerializerMethodField(method_name='get_price')
    purchase_price = serializers.SerializerMethodField(method_name='get_purchase_price')

    def get_price(self,obj):
        product_price = ProductPrice.objects.get(product=obj,currency=obj.enterprise.currency_default)
        return product_price.price
        
    def get_purchase_price(self,obj):
        product_price = ProductPrice.objects.get(product=obj,currency=obj.enterprise.currency_default)
        return product_price.purchase_price
    class Meta:
        model = Product
        fields = "__all__"
        
    expandable_fields ={
        'provider': ProviderSerializer,
        'category': ProductCategorySerializer,
        'enterprise': EnterpriseSerializer
    }